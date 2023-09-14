from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import (ProductDetailView, ProductCreateView, ProductListView, ContactListView, ProductUpdateView,
                           CategoryListView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('add_product/', never_cache(ProductCreateView.as_view()), name='add_product'),
    path('edit_product/<int:pk>', never_cache(ProductUpdateView.as_view()), name='edit_product'),
    path('categories/', CategoryListView.as_view(), name='categories'),
]
