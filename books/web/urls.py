from django.urls import path, include

from web import views


app_name = 'web'

urlpatterns = [
    path(route='books/<int:pk>/update', view=views.BookUpdateView.as_view(), name='book_update_form'),
    path(route='books/<int:pk>/delete/', view=views.BookDeleteView.as_view(), name='book_confirm_delete'),
    path(route='books/<int:pk>/', view=views.BookDetailView.as_view(), name='book_detail'),
    path(route='books/add/', view=views.BookCreateView.as_view(), name='book_form'),
    path(route='books/', view=views.BookListView.as_view(), name='book_list'),
    path(route='search/', view=views.SearchResultView.as_view(), name='search'),
    path(route='profile/', view=views.profile_view, name='profile'),
    path(route='login/', view=views.WebLoginView.as_view(), name='login'),
    path(route='logout/', view=views.WebLogoutView.as_view(), name='logout'),

    path(route='register/', view=views.RegisterView.as_view(), name='register'),
    path(route='register_confirm/<token>', view=views.register_confirm, name='register_confirm'),

    path(route='password_change/', view=views.ChangePasswordView.as_view(), name='password_change'),
    path(route='password_change_done/', view=views.ChangePasswordDoneView.as_view(), name='password_change_done'),

    path(route='password_reset/', view=views.ResetPasswordView.as_view(), name='password_reset'),
    path(route='password_reset/done/', view=views.ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path(route='reset/<token>/', view=views.reset_password_confirm, name="password_reset_confirm"),
    # path('accounts/', include('django.contrib.auth.urls')), # django: auth
]


handler404 = views.page_404
