from rest_framework.test import APITestCase

from web.models import *


# class ModelTest(APITestCase):
#     def setUp(self):
#         self.user = Reader.objects.create(
#             username="test_admin",
#             # email='admin@test.com',
#             password="Ololo965",
#             is_staff=True,
#         )

#         self.book = Book.objects.create(
#             title="Книга 1", 
#             author="Автор 1",
#             about='', 
#             added_by=self.user,
#         )


#     def test_book_field_title_max_length(self):
#         book = Book.objects.all()[0]
#         max_length = book._meta.get_field("title").max_length
#         self.assertEqual(max_length, 255)

#     def test_book_field_author_max_length(self):
#         book = Book.objects.all()[0]
#         max_length = book._meta.get_field("author").max_length
#         self.assertEqual(max_length, 100)

#     def test_book_field_about_max_length(self):
#         book = Book.objects.all()[0]
#         max_length = book._meta.get_field("about").max_length
#         self.assertEqual(max_length, 500)

#     def test_about_can_be_blank(self):
#         """Book's field about can be blank and default value will be empty string"""
#         book = Book.objects.all()[0]
#         blank_value = book._meta.get_field("about").blank
#         default_value = book._meta.get_field("about").default
#         self.assertEqual(blank_value, True)
#         self.assertEqual(default_value, "")

#     def test_about_is_not_blank(self):
#         book = Book.objects.all()[0]
#         book.about = "Здесь будет описание книги"
#         book.save()
#         self.assertEqual(book.about, "Здесь будет описание книги")

#     def test_added_by_after_deleting_is_none(self):
#         """After deleting an user Book's field added_by is None"""
#         Reader.objects.all()[0].delete()
#         book_owner = Book.objects.all()[0].added_by
#         self.assertEqual(book_owner, None)

#     def test_added_by_can_be_none(self):
#         """Book's field added_by can be None"""
#         book = Book.objects.create(title="Книга 1", author="Автор 1")
#         book_owner = book.added_by
#         self.assertEqual(book_owner, None)
