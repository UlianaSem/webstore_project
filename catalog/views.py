from django.forms import inlineformset_factory
from django.shortcuts import redirect

from catalog.forms import ProductForm, VersionForm, CustomInlineFormSet
from catalog.models import Product, ContactData, Version, Category
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from catalog.services import get_cache_categories


class ProductListView(ListView):
    paginate_by = 12
    model = Product
    extra_context = {
        'title': 'Главная страница'
    }


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

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, formset=CustomInlineFormSet, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data["formset"] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        self.object.owner = self.request.user
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        else:
            return self.form_invalid(form)

        return super().form_valid(form)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }

    def get_queryset(self):
        return get_cache_categories()
