from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    telephone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    code = models.CharField(max_length=4, verbose_name='код', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name="пользователь активен")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
