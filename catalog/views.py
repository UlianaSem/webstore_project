from django.shortcuts import render
from catalog.models import Product, ContactData


def home(request):
    print(Product.objects.reverse()[:5])

    context = {
        'object_list': Product.objects.all(),
        'title': 'Главная страница'
    }

    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'User {name} asks to contact her/him by email {email}')

    context = {
        'object_list': ContactData.objects.get(pk=1),
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    context = {
        'object_list': Product.objects.get(pk=pk),
        'title': 'Страница товара'
    }

    return render(request, 'catalog/product.html', context)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        picture = request.POST.get('picture')
        price = request.POST.get('price')

        Product.objects.create(
            name=name,
            description=description,
            picture=picture,
            price=float(price)
        )

    context = {
        'title': 'Предложите товар'
    }

    return render(request, 'catalog/add_product.html', context)
