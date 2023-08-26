from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'create_data', 'is_published', 'view_count']
    list_filter = ['is_published', 'create_data', 'view_count']
    search_fields = ['title', 'create_data']
