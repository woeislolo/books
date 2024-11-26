from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(Reader)
class ReaderAdmin(ModelAdmin):
    list_display = ('id', 'username', 'email') 
    list_display_links = ('id', 'username', 'email') 
    

@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('id', 'title', 'author', 'about', 'added_by') 
    list_display_links = ('id', 'title')
    

@admin.register(UserBookRelation)
class UserBookRelationAdmin(ModelAdmin):
    list_display = ('user', 'book', 'like', 'in_bookmarks', 'rate')
