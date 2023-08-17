from django.contrib import admin
from catalog.models import Category, Product, ContactData


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price', 'category_id']
    list_filter = ['category_id']
    search_fields = ['name', 'description']


@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ['pk', 'address', 'telephone_number', 'email']
    search_fields = ['address']
