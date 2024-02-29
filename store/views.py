from django.shortcuts import render, redirect

from .forms import AddProductForm
from .models import Store, Product


def get_store_page(request):
    stores = Store.objects.all()
    products = Product.objects.all()
    print(products)
    context = {
        'stores': stores,
        'products': products

    }

    return render(request, 'index.html', context)


def get_add_product_page(request):
    stores = Store.objects.all()
    products = Product.objects.all()
    form = AddProductForm()
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            colors = form.cleaned_data.pop('colors')
            new_product = Product(**form.cleaned_data)
            new_product.save()
            new_product.colors.set(colors)  # устанавливаем связь между экземпляром класса и цветами
            return redirect('home')
        else:
            print(form.errors)
            print(form.cleaned_data)
    context = {
        'stores': stores,
        'products': products,
        'form': form
    }
    return render(request, 'add_product.html', context)


def get_description_page(request, id):
    products = Product.objects.get(id=id)
    print(products.colors.all())

    context = {
        'products': products
    }
    return render(request, 'description.html', context)


def get_product_from_store(request, id):
    store = Store.objects.get(id=id)
    products_by_store = store.product_set.all()
    context = {
        'products_by_store': products_by_store
    }
    return render(request, 'get_prod_from_store.html', context)


