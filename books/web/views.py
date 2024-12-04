import secrets
import string
import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import PasswordResetDoneView, \
    PasswordChangeView, PasswordChangeDoneView, LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import Http404

from .models import *
from .forms import *
from books.settings import *


def page_404(request):
    raise Http404()


class BookListView(ListView):
    model = Book
    context_object_name = 'books'


class BookDetailView(DetailView):
    queryset = Book.objects.prefetch_related('readers')
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = LOGIN_URL
    model = Book
    form_class = BookForm
    success_message = "Книга %(title)s, %(author)s успешно добавлена."


class BookUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'web.change_book'
    login_url = LOGIN_URL
    model = Book
    form_class = BookForm
    template_name_suffix = '_update_form'
    context_object_name = 'book'


class BookDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'web.delete_book'
    login_url = LOGIN_URL
    model = Book
    success_url = reverse_lazy("web:book_list")


class SearchResult(ListView):
    model = Book
    template_name = 'web/search.html'
    context_object_name = 'books'
    result_num = 0
    query = ''

    def get_queryset(self):
        self.query = self.request.GET.get('q', '')
        searched_books = Book.objects.filter(
            Q(title__contains=self.query) | Q(author__contains=self.query))
        self.result_num = len(searched_books)
        return searched_books


@login_required
def profile_view(request):
    return render(request=request, template_name='web/profile.html') 


class WebLoginView(LoginView):
    template_name = "registration/login.html"
    success_url = 'web:profile'


class WebLogoutView(LogoutView):
    template_name = "registration/logged_out.html"
    success_url = 'web:book_list'


class ChangePasswordView(PasswordChangeView):
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("web:password_change_done")


class ChangePasswordDoneView(PasswordChangeDoneView):
    ...


class RegisterView(SuccessMessageMixin, FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("web:book_list")
    success_message = "Ссылка для активации аккаунта отправлена на %(email)s."

    def form_valid(self, form):
        reader, created = Reader.objects.get_or_create(email=form.cleaned_data['email']) 
        new_pass = None

        if created or reader.is_active is False:
            alphabet = string.ascii_letters + string.digits
            new_pass = ''.join(secrets.choice(alphabet) for i in range(8))
            reader.set_password(new_pass)
            reader.username = form.cleaned_data['username']
            reader.save(update_fields=['password', 'username'])

            token = uuid.uuid4().hex
            redis_key = BOOKS_APP_USER_CONFIRMATION_KEY.format(token=token)
            cache.set(redis_key, {'reader_id': reader.id}, timeout=BOOKS_APP_USER_CONFIRMATION_TIMEOUT)

            confirm_link = self.request.build_absolute_uri(
                reverse_lazy(
                    'web:register_confirm', kwargs={'token': token}
                )
            )
            message = f'Ваш пароль - {new_pass}. Перейдите по ссылке для активации аккаунта: {confirm_link}'

            send_mail(
                subject="Подтверждение регистрации",
                message=message,
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[reader.email,],
            )

        return super().form_valid(form)


def register_confirm(request, token):
    redis_key = BOOKS_APP_USER_CONFIRMATION_KEY.format(token=token)
    reader_info = cache.get(redis_key) or {}

    if reader_id := reader_info.get('reader_id'):
        reader = get_object_or_404(Reader, id=reader_id)
        reader.is_active = True
        reader.save(update_fields=['is_active'])
        return redirect(reverse_lazy('web:profile'))
    else:
        return redirect(reverse_lazy('web:register'))


class ResetPasswordView(SuccessMessageMixin, FormView):
    form_class = ResetPasswordForm
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy("web:password_reset_done")
    success_message = "Ссылка для сброса пароля отправлена на почту %(email)s."

    def form_valid(self, form):
        reader = get_object_or_404(Reader, email=form.cleaned_data['email'])

        if reader:
            alphabet = string.ascii_letters + string.digits
            new_pass = ''.join(secrets.choice(alphabet) for i in range(8))
            reader.set_password(new_pass)
            reader.save(update_fields=['password',])

            token = uuid.uuid4().hex
            redis_key = BOOKS_APP_USER_RESET_PASSWORD_KEY.format(token=token)
            cache.set(redis_key, {'reader_id': reader.id}, timeout=BOOKS_APP_USER_RESET_PASSWORD_TIMEOUT)

            reset_pass_link = self.request.build_absolute_uri(
                reverse_lazy(
                    'web:password_reset_confirm', kwargs={'token': token}
                )
            )
            message = f'Ваш новый пароль - {new_pass}. Перейдите по ссылке для сброса пароля: {reset_pass_link}'

            print(message)

            send_mail(
                subject="Сброс пароля",
                message=message,
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[reader.email,],
            )

            # TODO: вынести генерацию пароля и токена (дублируется в 2х функциях)

            return super().form_valid(form)


class ResetPasswordDoneView(PasswordResetDoneView):
    ...


def reset_password_confirm(request, token):
    redis_key = BOOKS_APP_USER_RESET_PASSWORD_KEY.format(token=token)
    reader_info = cache.get(redis_key) or {}

    if reader_id := reader_info.get('reader_id'):
        return redirect(reverse_lazy('web:login'))
    else:
        return redirect(reverse_lazy('web:password_reset'))
