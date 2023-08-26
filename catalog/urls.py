from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import ProductDetailView, ProductCreateView, ProductListView, ContactListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
]
