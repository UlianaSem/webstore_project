from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.forms import inlineformset_factory
from django.shortcuts import redirect

from catalog.forms import ProductForm, VersionForm, CustomInlineFormSet,ProductModeratorForm
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


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = {"Owner": ProductForm, "Moderator": ProductModeratorForm}
    permission_required = {"Owner": ['catalog.change_product'],
                           "Moderator": ['catalog.set_published', 'catalog.change_description',
                                         'catalog.change_category']}

    def has_permission(self):
        perms = self.get_permission_required()

        if self.request.user == self.get_object().owner:

            perms = perms.get("Owner")

        elif "Moderator" in [group.name for group in self.request.user.groups.all()]:
            perms = perms.get("Moderator")

        else:
            return False

        return self.request.user.has_perms(perms)

    def get_form_class(self):
        form_class = super().get_form_class()

        if self.request.user == self.get_object().owner:
            return form_class.get("Owner")

        elif "Moderator" in [group.name for group in self.request.user.groups.all()]:
            return form_class.get("Moderator")

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


class ProductsByCategory(ListView):
    paginate_by = 12
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Продукты категории {category_item.name.lower()}'

        return context_data
