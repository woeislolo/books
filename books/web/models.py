from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Reader(AbstractUser):

    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[AbstractUser.username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        null=True,
        blank=True,
    )

    email = models.EmailField(_("email address"), unique=True)

    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    about = models.CharField(max_length=500, blank=True, default='', verbose_name='О книге')
    added_by = models.ForeignKey(Reader, null=True, on_delete=models.SET_NULL, related_name='my_books', verbose_name='Кем добавлено')
    readers = models.ManyToManyField(to=Reader, through='UserBookRelation', related_name='books', verbose_name='Читатели')


    def __str__(self):
        return f'{self.title}, {self.author}'
    
    def get_absolute_url(self):
        return reverse(viewname='web:book_detail', kwargs={'pk': self.pk}) 
    
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги' 
        ordering = ('id',)


class UserBookRelation(models.Model):
    RATE_CHOISE = (
        (1, 'Bad'),
        (2, 'Ok'),
        (3, 'Good')
    )
    user = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOISE, null=True)


    def __str__(self):
        return f'{self.book.title}, {self.user.username}, Like: {self.like}, Bookmark: {self.in_bookmarks}, Rate: {self.rate}'


    class Meta:
        verbose_name = "Связь 'пользователь-книга': лайк, закладка, рейтинг"
        ordering = ('id',)
