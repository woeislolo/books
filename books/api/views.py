from django.db.models import Count, Avg, Case, When

from rest_framework import viewsets
from rest_framework.mixins import UpdateModelMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework_simplejwt.authentication import JWTAuthentication

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .permissions import *
from web.models import *


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'username']
    ordering = ['id']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().annotate(
        annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
        rating=Avg('userbookrelation__rate')
        ).order_by("id")
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrAddedByOrReadOnly,)
    authentication_classes = (TokenAuthentication, JWTAuthentication)

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author'] # ?author=Автор
    search_fields = ['title', 'author'] # ?search=Автор
    ordering_fields = ['title', 'author'] # ?ordering=author
    ordering = ['id'] # default ordering

    def perform_create(self, serializer):
        serializer.validated_data['added_by'] = self.request.user
        serializer.save()


class UserBookRelationView(UpdateModelMixin, viewsets.GenericViewSet):
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookRelationSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, JWTAuthentication)
    lookup_field = 'book'  # в урле будет передан параметр, 
        # который внутри вью называется 'book'
        # можно получить через self.kwargs['book']

    def get_object(self):
        obj, _ = UserBookRelation.objects.get_or_create(
            user=self.request.user,
            book_id=self.kwargs['book'])
        return obj