from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование', unique=True)
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование', unique=True)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    picture = models.ImageField(upload_to='catalog/', verbose_name='изображение', **NULLABLE)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, **NULLABLE)
    price = models.FloatField(verbose_name='цена', **NULLABLE)
    create_date = models.DateField(verbose_name='дата создания', **NULLABLE, auto_now_add=True)
    change_date = models.DateField(verbose_name='дата изменения', **NULLABLE, auto_now=True)
    is_published = models.BooleanField(verbose_name="опубликовано", default=False)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.price} в категории {self.category_id}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            (
                'set_published', 'Can publish product'
            ),
            (
                'change_description', 'Can change product description'
            ),
            (
                'change_category', 'Can change product category'
            ),
        ]


class ContactData(models.Model):
    address = models.CharField(max_length=300, verbose_name='адрес')
    telephone_number = models.CharField(max_length=50, verbose_name='номер телефона')
    email = models.EmailField(max_length=100, verbose_name='email', **NULLABLE)

    def __str__(self):
        return f'{self.address}\n{self.telephone_number}'

    class Meta:
        verbose_name = 'контактные данные'
        verbose_name_plural = 'контактные данные'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='активна')

    def __str__(self):
        return f'{self.product} версия {self.number} ({self.is_active})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
