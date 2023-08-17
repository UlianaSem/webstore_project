import json

from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    PATH = 'catalog_data.json'

    def handle(self, *args, **options):
        data = self.open_file__()
        categories_for_create = []
        products_for_create = []

        Category.objects.all().delete()
        Product.objects.all().delete()

        for item in data:
            if item['model'] == "catalog.category":
                categories_for_create.append(Category(**item['fields']))

        Category.objects.bulk_create(categories_for_create)

        for item in data:
            if item['model'] == "catalog.product":
                product_name = self.search_category_name__(data, item['fields']['category_id'])
                item['fields']['category_id'] = Category.objects.get(name=product_name)
                products_for_create.append(Product(**item['fields']))

        Product.objects.bulk_create(products_for_create)

    @classmethod
    def open_file__(cls):
        with open(cls.PATH, 'r', encoding='utf-8') as file:
            data_for_open = file.read()

        json_data = json.loads(data_for_open)

        return json_data

    @staticmethod
    def search_category_name__(data, id_):
        for item in data:
            if item['model'] == "catalog.category" and id_ == item['pk']:
                return item['fields']['name']
