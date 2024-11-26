from django.db.models import Count, Avg, Case, When

from rest_framework.test import APITestCase

from web.models import *
from ..serializers import *


# class UserSerializerTestCase(APITestCase):
#     def setUp(self):
#         self.admin = Reader.objects.create(
#             username="test_admin", password="Ololo965", is_staff=True
#         )

#         self.user = Reader.objects.create(
#             username="test_user", password="Ololo965", is_staff=False
#         )

#     def test_user_serializer(self):
#         users = Reader.objects.all()
#         serializer_data = UserSerializer(users, many=True).data
#         expected_data = [
#             {
#                 "id": self.admin.id,
#                 "username": "test_admin",
#             },
#             {
#                 "id": self.user.id,
#                 "username": "test_user",
#             },
#         ]
#         self.assertEqual(expected_data, serializer_data)


# class BookSerializerTestCase(APITestCase):
#     def setUp(self):
#         self.admin = Reader.objects.create(
#             username="test_admin", password="Ololo965", is_staff=True
#         )

#         self.user1 = Reader.objects.create(
#             username="test_user", password="Ololo965", is_staff=False
#         )

#         self.user2 = Reader.objects.create(
#             username="test_user2", password="Ololo965", is_staff=False
#         )

#         self.book1 = Book.objects.create(
#             title="Книга 2", author="Автор 2", added_by=self.admin
#         )
#         self.book2 = Book.objects.create(
#             title="Книга 3", author="Автор 3", added_by=self.user1
#         )

#         UserBookRelation.objects.create(
#             user=self.user1, book=self.book1, like=True, rate=5
#         )
#         UserBookRelation.objects.create(
#             user=self.user2, book=self.book1, like=True, rate=4
#         )
#         UserBookRelation.objects.create(user=self.admin, book=self.book1, like=False)

#         UserBookRelation.objects.create(user=self.user1, book=self.book2, like=True)
#         UserBookRelation.objects.create(
#             user=self.user2, book=self.book2, like=False, rate=3
#         )
#         UserBookRelation.objects.create(
#             user=self.admin, book=self.book2, like=True, rate=3
#         )

#     def test_book_serializer(self):
#         books = (
#             Book.objects.all()
#             .annotate(
#                 annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
#                 rating=Avg("userbookrelation__rate"),
#             )
#             .order_by("id")
#         )

#         serializer_data = BookSerializer(books, many=True).data

#         expected_data = [
#             {
#                 "id": self.book1.id,
#                 "title": "Книга 2",
#                 "author": "Автор 2",
#                 "about": "",
#                 "added_by": self.admin.id,
#                 "readers": [
#                     {"id": self.admin.id, "username": self.admin.username},
#                     {"id": self.user1.id, "username": self.user1.username},
#                     {"id": self.user2.id, "username": self.user2.username},
#                 ],
#                 "annotated_likes": 2,
#                 "rating": "4.5",
#             },
#             {
#                 "id": self.book2.id,
#                 "title": "Книга 3",
#                 "author": "Автор 3",
#                 "about": "",
#                 "added_by": self.user1.id,
#                 "readers": [
#                     {"id": self.admin.id, "username": self.admin.username},
#                     {"id": self.user1.id, "username": self.user1.username},
#                     {"id": self.user2.id, "username": self.user2.username},
#                 ],
#                 "annotated_likes": 2,
#                 "rating": "3.0",
#             },
#         ]

#         self.assertEqual(expected_data, serializer_data)

