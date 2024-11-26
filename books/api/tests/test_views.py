from django.db.models import Count, Avg, Case, When
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from ..serializers import *
from web.models import *


# class BookGetAPITestCase(APITestCase):
#     def setUp(self):
#         self.admin = Reader.objects.create(
#             username="test_admin", 
#             password="Ololo965", 
#             is_staff=True
#         )

#         self.user = Reader.objects.create(
#             username="test_user", 
#             password="Ololo965", 
#             is_staff=False
#         )

#         self.user_book = Book.objects.create(
#             title="Книга Юзера",
#             author="Автор Юзера",
#             added_by=self.user,
#         )

#         self.admin_book = Book.objects.create(
#             title="Книга Админа",
#             author="Автор Админа",
#             added_by=self.admin,
#         )

#         self.user_book_2 = Book.objects.create(
#             title="Книга 2",
#             author="Юзер 2",
#             added_by=self.user,
#         )

#         self.user_book_3 = Book.objects.create(
#             title="Книга 3",
#             author="Автор Админа",
#             added_by=self.user,
#         )

#         UserBookRelation.objects.create(book=self.user_book, user=self.user, like=True, rate=1)
#         UserBookRelation.objects.create(book=self.user_book, user=self.admin, like=True, rate=5)

#     def tearDown(self):
#         self.client.force_authenticate(user=None) # отменить аутентификацию

# # get all ordering
#     def test_get_books_by_unauthorized_user(self):
#         books = Book.objects.all().annotate(
#             annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
#             rating=Avg('userbookrelation__rate')
#             ).order_by("id")
#         url = reverse("books-list")
#         response = self.client.get(url, format='json')
#         serializer_data = BookSerializer(books, many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
    
#         self.assertEqual(serializer_data, response.data['results'])
#         self.assertEqual(serializer_data[0]['rating'], '3.0')
#         self.assertEqual(serializer_data[0]['annotated_likes'], 2)


#     def test_get_books_by_authorized_user(self):
#         books = Book.objects.all().annotate(
#             annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
#             rating=Avg('userbookrelation__rate')
#             ).order_by("id")
#         url = reverse("books-list")
#         self.client.force_authenticate(self.user)
#         response = self.client.get(url, format='json')
#         serializer_data = BookSerializer(books, many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data['results'])

#     def test_get_books_by_admin(self):
#         books = Book.objects.all().annotate(
#             annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
#             rating=Avg('userbookrelation__rate')
#             ).order_by("id")
#         url = reverse("books-list")
#         self.client.force_authenticate(self.admin)
#         response = self.client.get(url, format='json')
#         serializer_data = BookSerializer(books, many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data['results'])

# # get all filter
#     def test_get_filter_books(self):
#         books = Book.objects.filter(id__in=[self.admin_book.id, self.user_book_3.id]).annotate(
#             annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
#             rating=Avg('userbookrelation__rate')
#             ).order_by("id").order_by('id')
#         url = reverse("books-list")
#         filter_data = {'author': 'Автор Админа'}
#         response = self.client.get(url, data=filter_data, format='json')
#         serializer_data = BookSerializer(books, many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data['results'], response.data)

# # get all search
#     def test_get_search_books(self):
#         books = Book.objects.filter(
#             id__in=[self.user_book.id, self.admin_book.id, self.user_book_3.id]).annotate(
#             annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
#             rating=Avg('userbookrelation__rate')
#             ).order_by("id")
#         url = reverse("books-list")
#         search_data = {'search': 'Автор'}
#         response = self.client.get(url, data=search_data, format='json')
#         serializer_data = BookSerializer(books, many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data['results'])


# # get one
#     def test_get_book_by_unauthorized_user(self):
#         book = Book.objects.filter(id=self.user_book.id).annotate(
#             annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
#             rating=Avg('userbookrelation__rate')
#             ).order_by("id")      
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         response = self.client.get(url, format='json')
#         serializer_data = BookSerializer(book, many=True).data[0]
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data)

#     def test_get_book_by_authorized_user(self):
#         book = Book.objects.filter(id=self.user_book.id).annotate(
#             annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
#             rating=Avg('userbookrelation__rate')
#             ).order_by("id")
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         self.client.force_authenticate(self.user)
#         response = self.client.get(url, format='json')
#         serializer_data = BookSerializer(book, many=True).data[0]
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data)

#     def test_get_book_by_admin(self):
#         book = Book.objects.filter(id=self.user_book.id).annotate(
#             annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
#             rating=Avg('userbookrelation__rate')
#             ).order_by("id")
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         self.client.force_authenticate(self.admin)
#         response = self.client.get(url, format='json')
#         serializer_data = BookSerializer(book, many=True).data[0]
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data)


# class BookCreateAPITestCase(APITestCase):
#     def setUp(self):
#         self.admin = UReaderser.objects.create(
#             username="test_admin", 
#             password="Ololo965", 
#             is_staff=True
#         )

#         self.user = Reader.objects.create(
#             username="test_user", 
#             password="Ololo965", 
#             is_staff=False
#         )

#     def tearDown(self):
#         self.client.force_authenticate(user=None)

# # create
#     def test_create_book_by_unauthorised_user(self):
#         url = reverse('books-list')
#         data = {'title': 'Книга', 'author': 'Автор'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)


#     def test_create_book_by_authorised_user(self):
#         self.assertEqual(0, Book.objects.all().count())
#         url = reverse('books-list')
#         self.client.force_authenticate(self.user)
#         data = {'title': 'Книга Юзера 2', 'author': 'Автор Юзера', 'added_by': self.user.pk}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#         self.assertEqual('Книга Юзера 2', response.data['title'])
#         self.assertEqual('Автор Юзера', response.data['author'])
#         self.assertEqual(1, Book.objects.all().count())
#         self.assertEqual(self.user, Book.objects.last().added_by)
        

#     def test_create_book_by_authorised_user_without_title(self):
#         url = reverse('books-list')
#         self.client.force_authenticate(self.user)
#         data = {'author': 'Автор Юзера'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_book_by_authorised_user_without_author(self):
#         url = reverse('books-list')
#         self.client.force_authenticate(self.user)
#         data = {'title': 'Книга Юзера'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


#     def test_create_book_by_admin(self):
#         self.assertEqual(0, Book.objects.all().count())
#         url = reverse('books-list')
#         self.client.force_authenticate(self.admin)
#         data = {'title': 'Книга Админа 2', 'author': 'Автор Админа', 'added_by': self.admin.pk}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#         self.assertEqual('Книга Админа 2', response.data['title'])
#         self.assertEqual('Автор Админа', response.data['author'])
#         self.assertEqual(1, Book.objects.all().count())
#         self.assertEqual(self.admin, Book.objects.last().added_by) # perfrom_create


#     def test_create_book_by_admin_without_title(self):
#         url = reverse('books-list')
#         self.client.force_authenticate(self.admin)
#         data = {'author': 'Автор Админа'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_book_by_admin_without_author(self):
#         url = reverse('books-list')
#         self.client.force_authenticate(self.admin)
#         data = {'title': 'Книга Админа'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class BookUpdateAPITestCase(APITestCase):
#     def setUp(self):
#         self.admin = Reader.objects.create(
#             username="admin", 
#             password="Ololo965", 
#             is_staff=True
#         )

#         self.user = Reader.objects.create(
#             username="user", 
#             password="Ololo965", 
#             is_staff=False
#         )

#         self.user_book = Book.objects.create(
#             title="Книга Юзера",
#             author="Автор Юзера",
#             added_by=self.user,
#         )

#         self.admin_book = Book.objects.create(
#             title="Книга Админа",
#             author="Автор Админа",
#             added_by=self.admin,
#         )  

#     def tearDown(self):
#         self.client.force_authenticate(user=None)

#     def test_update_book_by_unauthorised_user(self):
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         book_data = {
#             'title': 'Измененная книга', 
#             'author': 'Измененный автор',
#             'about': '',
#             'added_by': self.user.id,
#             }
#         response = self.client.put(url, book_data, format='json')
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

#     def test_update_user_book_by_authorised_user(self):
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         book_data = {
#             'title': 'Измененная книга', 
#             'author': 'Измененный автор',
#             'about': '',
#             'added_by': self.user.id,
#             }
#         self.client.force_authenticate(self.user)
#         response = self.client.put(url, book_data, format='json')
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.user_book.refresh_from_db()
#         self.assertEqual(self.user_book.title, 'Измененная книга')
#         self.assertEqual(self.user_book.author, 'Измененный автор')


#     def test_update_admin_book_by_authorised_user(self):
#         url = reverse("books-detail", kwargs={'pk': self.admin_book.id})
#         book_data = {
#             'title': 'Измененная книга', 
#             'author': 'Измененный автор',
#             'about': '',
#             'added_by': self.admin.id,
#             }
#         self.client.force_authenticate(self.user)
#         response = self.client.put(url, book_data, format='json')
#         self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

#     def test_update_user_book_by_admin(self):
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         book_data = {
#             'title': 'Измененная книга', 
#             'author': 'Измененный автор',
#             'about': '',
#             'added_by': self.user.id,
#             }
#         self.client.force_authenticate(self.admin)
#         response = self.client.put(url, book_data, format='json')
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.user_book.refresh_from_db()
#         self.assertEqual(self.user_book.title, 'Измененная книга')
#         self.assertEqual(self.user_book.author, 'Измененный автор')

#     def test_update_admin_book_by_admin(self):
#         url = reverse("books-detail", kwargs={'pk': self.admin_book.id})
#         book_data = {
#             'title': 'Измененная книга', 
#             'author': 'Измененный автор',
#             'about': '',
#             'added_by': self.admin.id,
#             }
#         self.client.force_authenticate(self.admin)
#         response = self.client.put(url, book_data, format='json')
#         self.admin_book.refresh_from_db()
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(self.admin_book.title, 'Измененная книга')
#         self.assertEqual(self.admin_book.author, 'Измененный автор')

# # partial update

#     def test_partial_update_book_by_unauthorised_user(self):
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         book_data = {'title': 'Измененная книга '}
#         response = self.client.patch(url, book_data, format='json')
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

#     def test_partial_update_user_book_by_authorised_user(self):
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         book_data = {'title': 'Измененная книга'}
#         self.client.force_authenticate(self.user)
#         response = self.client.patch(url, book_data, format='json')
#         self.user_book.refresh_from_db()
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(self.user_book.title, 'Измененная книга')

#     def test_partial_update_admin_book_by_authorised_user(self):
#         url = reverse("books-detail", kwargs={'pk': self.admin_book.id})
#         book_data = {'title': 'Измененная книга'}
#         self.client.force_authenticate(self.user)
#         response = self.client.patch(url, book_data, format='json')
#         self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

#     def test_partial_update_user_book_by_admin(self):
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         book_data = {'title': 'Измененная книга'}
#         self.client.force_authenticate(self.admin)
#         response = self.client.patch(url, book_data, format='json')
#         self.user_book.refresh_from_db()
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(self.user_book.title, 'Измененная книга')

#     def test_partial_update_admin_book_by_admin(self):
#         url = reverse("books-detail", kwargs={'pk': self.admin_book.id})
#         book_data = {'title': 'Измененная книга'}
#         self.client.force_authenticate(self.admin)
#         response = self.client.patch(url, book_data, format='json')
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.admin_book.refresh_from_db()
#         self.assertEqual(self.admin_book.title, 'Измененная книга')


# class BookDeleteAPITestCase(APITestCase):
#     def setUp(self):
#         self.admin = Reader.objects.create(
#             username="test_admin", 
#             password="Ololo965", 
#             is_staff=True
#         )

#         self.user = Reader.objects.create(
#             username="test_user", 
#             password="Ololo965", 
#             is_staff=False
#         )

#         self.user_book = Book.objects.create(
#             title="Книга Юзера",
#             author="Автор Юзера",
#             added_by=self.user,
#         )

#         self.admin_book = Book.objects.create(
#             title="Книга Админа",
#             author="Автор Админа",
#             added_by=self.admin,
#         )    

#     def tearDown(self):
#         self.client.force_authenticate(user=None)

#     def test_delete_user_book_by_unauthorised_user(self):
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         response = self.client.delete(url, format='json')
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)


#     def test_delete_user_book_by_authorised_user(self):
#         self.assertEqual(2, Book.objects.all().count())
#         url = reverse('books-detail', kwargs={'pk': self.user_book.id})
#         self.client.force_authenticate(self.user)
#         response = self.client.delete(url, format='json')
#         self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
#         self.assertEqual(1, Book.objects.all().count())

#     def test_delete_admin_book_by_authorised_user(self):
#         url = reverse("books-detail", kwargs={'pk': self.admin_book.id})
#         self.client.force_authenticate(self.user)
#         response = self.client.delete(url, format='json')
#         self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code, response.data)


#     def test_delete_user_book_by_admin(self):
#         self.assertEqual(2, Book.objects.all().count())
#         url = reverse("books-detail", kwargs={'pk': self.user_book.id})
#         self.client.force_authenticate(self.admin)
#         response = self.client.delete(url, format='json')
#         self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
#         self.assertEqual(1, Book.objects.all().count())

#     def test_delete_admin_book_by_admin(self):
#         self.assertEqual(2, Book.objects.all().count())
#         url = reverse("books-detail", kwargs={'pk': self.admin_book.id})
#         self.client.force_authenticate(self.admin)
#         response = self.client.delete(url, format='json')
#         self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
#         self.assertEqual(1, Book.objects.all().count())


# class UserGetAPITestCase(APITestCase):
#     def setUp(self):
#         self.user = Reader.objects.create(
#             username="test_user", 
#             password="Ololo965", 
#             is_staff=False
#         )

#         self.admin = Reader.objects.create(
#             username="test_admin", 
#             password="Ololo965", 
#             is_staff=True
#         )

#     def tearDown(self):
#         self.client.force_authenticate(user=None)

#     def test_get_users_by_admin(self):
#         users = Reader.objects.all()
#         url = reverse("users-list")
#         self.client.force_authenticate(self.admin)
#         response = self.client.get(url, format='json')
#         serializer_data = UserSerializer(users, many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data['results'], response.data)

#     def test_get_user_by_admin(self):
#         # users = User.objects.all()
#         url = reverse("users-detail", kwargs={'pk':self.admin.id})
#         self.client.force_authenticate(self.admin)
#         response = self.client.get(url, format='json')
#         serializer_data = UserSerializer(self.admin).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data, response.data)


#     def test_get_users_by_user(self):
#         url = reverse("users-list")
#         self.client.force_authenticate(self.user)
#         response = self.client.get(url, format='json')
#         self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

#     def test_get_user_by_user(self):
#         url = reverse("users-detail", kwargs={'pk':self.admin.id})
#         self.client.force_authenticate(self.user)
#         response = self.client.get(url, format='json')
#         self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)


# class UserBookRelationAPITestCase(APITestCase):
#     def setUp(self):
#         self.admin = Reader.objects.create(
#             username="test_admin", 
#             password="Ololo965", 
#             is_staff=True
#         )

#         self.user = Reader.objects.create(
#             username="test_user", 
#             password="Ololo965", 
#             is_staff=False
#         )

#         self.user_book = Book.objects.create(
#             title="Книга Юзера",
#             author="Автор Юзера",
#             added_by=self.user,
#         )

#         self.admin_book = Book.objects.create(
#             title="Книга Админа",
#             author="Автор Админа",
#             added_by=self.admin,
#         )

#     def tearDown(self):
#         self.client.force_authenticate(user=None)

#     def test_like_userbook_by_admin(self):
#         url = reverse("userbookrelation-detail", kwargs={'book': self.user_book.id})
#         self.client.force_authenticate(self.admin)
#         data = {
#             'like': True,
#         }
#         response = self.client.patch(url, data=data, format='json')
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         relation = UserBookRelation.objects.get(user=self.admin, book=self.user_book)
#         self.assertTrue(relation.like)

#     def test_in_bookmarks_userbook_by_admin(self):
#         url = reverse("userbookrelation-detail", kwargs={'book': self.user_book.id})
#         self.client.force_authenticate(self.admin)
#         data = {
#             'in_bookmarks': True,
#         }
#         response = self.client.patch(url, data=data, format='json')
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         relation = UserBookRelation.objects.get(user=self.admin, book=self.user_book)
#         self.assertTrue(relation.in_bookmarks)

#     def test_rate_userbook_by_admin(self):
#         url = reverse("userbookrelation-detail", kwargs={'book': self.user_book.id})
#         self.client.force_authenticate(self.admin)
#         data = {
#             'rate': 3,
#         }
#         response = self.client.patch(url, data=data, format='json')
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         relation = UserBookRelation.objects.get(user=self.admin, book=self.user_book)
#         self.assertEqual(3, relation.rate)

#     def test_wrong_rate_userbook_by_admin(self):
#         url = reverse("userbookrelation-detail", kwargs={'book': self.user_book.id})
#         self.client.force_authenticate(self.admin)
#         data = {
#             'rate': 5,
#         }
#         response = self.client.patch(url, data=data, format='json')
#         self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code, response.data)


# # shift alt f
