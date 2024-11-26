from django.urls import path, include

from . import views


app_name = 'web'

urlpatterns = [
    path(route='books/<int:pk>/update', view=views.BookUpdateView.as_view(), name='book_update_form'),
    path(route='books/<int:pk>/delete/', view=views.BookDeleteView.as_view(), name='book_confirm_delete'),
    path(route='books/<int:pk>/', view=views.BookDetailView.as_view(), name='book_detail'),
    path(route='books/add/', view=views.BookCreateView.as_view(), name='book_form'),
    path(route='books/', view=views.BookListView.as_view(), name='book_list'),

    path(route='profile/', view=views.profile_view, name='profile'),
    path(route='register/', view=views.RegisterView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')), # django: auth
    path(route='search/', view=views.SearchResult.as_view(), name='search'),
]