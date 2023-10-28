"""Задание 1
Продолжаем работать с проектом. Создайте группу для роли модератора и опишите необходимые доступы:
    может отменять публикацию продукта,
    может менять описание любого продукта,
    может менять категорию любого продукта."""
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        group = Group.objects.create(
            name="Moderator"
        )

        content_type = ContentType.objects.get_for_model(Product)
        permission_list = Permission.objects.filter(codename__in=['set_published', 'change_description',
                                                                  'change_category'],
                                                    content_type=content_type, )

        group.permissions.set(permission_list)
        group.save()
