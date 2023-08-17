from django.shortcuts import render
from catalog.models import Product


def home(request):
    print(Product.objects.reverse()[:5])

    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'User {name} asks to contact her/him by email {email}')
    return render(request, 'catalog/contacts.html')
