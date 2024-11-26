from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'users', UserViewSet, basename='users')
router.register(r'book_relation', UserBookRelationView)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]