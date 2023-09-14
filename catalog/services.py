from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_cache_categories():
    if settings.CACHE_ENABLED:
        key = 'categories_list'
        queryset = cache.get(key)

        if queryset is None:
            queryset = Category.objects.all()
            cache.set(key, queryset)

    else:
        queryset = Category.objects.all()

    return queryset
