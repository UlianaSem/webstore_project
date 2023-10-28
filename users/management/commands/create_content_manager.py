from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from blog.models import Blog


class Command(BaseCommand):

    def handle(self, *args, **options):
        group = Group.objects.create(
            name="Content manager"
        )

        content_type = ContentType.objects.get_for_model(Blog)
        permission_list = Permission.objects.filter(codename__in=['add_blog', 'change_blog', 'delete_blog'],
                                                    content_type=content_type, )

        group.permissions.set(permission_list)
        group.save()
