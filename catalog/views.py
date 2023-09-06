from django.shortcuts import redirect

from catalog.forms import ProductForm
from catalog.models import Product, ContactData, Version
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy


"""
При наличии активной версии реализуйте вывод в список продуктов информации об активной версии."""

class ProductListView(ListView):
    paginate_by = 12
    model = Product
    extra_context = {
        'title': 'Главная страница'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        length = len(queryset)
        print(queryset[length-5:length])

        return queryset


class ContactListView(ListView):
    model = ContactData
    extra_context = {
        'title': 'Контакты'
    }

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request)

        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            print(f'User {name} asks to contact her/him by email {email}')

            return redirect('catalog:home')

        return response


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Страница товара'
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
