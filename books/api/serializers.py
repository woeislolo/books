from rest_framework.serializers import ModelSerializer, IntegerField, DecimalField

from web.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = Reader
        fields = ['id', 'username']


class BookSerializer(ModelSerializer):
    readers = UserSerializer(many=True, read_only=True)
    annotated_likes = IntegerField(read_only=True)
    rating = DecimalField(max_digits=3, decimal_places=1, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'about', 'added_by', 'readers', 'annotated_likes', 'rating']


class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ['like', 'in_bookmarks', 'rate']
