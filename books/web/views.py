from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import *


@login_required
def profile_view(request):
    return render(request=request, template_name='web/profile.html') 


class BookListView(ListView):
    model = Book
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_update_form'
    context_object_name = 'book'


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("web:book_list")


class ProfileView(DetailView):
    model = Reader
    template_name = 'web/profile.html'
    context_object_name = 'user'


class RegisterView(CreateView):
    model = Reader
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("web:login")


class ResetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm


class SearchResult(ListView):
    model = Book
    template_name = 'web/search.html'
    context_object_name = 'books'
    result_num = 0
    query = ''

    def get_queryset(self):
        self.query = self.request.GET.get('q', '')
        searched_books = Book.objects.filter(Q(title__contains=self.query) | Q(author__contains=self.query))
        self.result_num = len(searched_books)
        return searched_books
