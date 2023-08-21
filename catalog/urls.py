from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import home, contacts, product, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product'),
    path('add_product/', add_product, name='add_product'),
]
