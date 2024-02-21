from django.shortcuts import render, redirect

from .forms import AddProductForm
from .models import Store, Product


# Create your views here.

def get_store_page(request):
    stores = Store.objects.all()
    products = Product.objects.all()

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
        form = AddProductForm(request.POST)
        if form.is_valid():
            new_product = Product(**form.cleaned_data)
            new_product.save()
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
    stores = Store.objects.all()
    products = Product.objects.get(id=id)

    context = {
        'stores': stores,
        'products': products
    }
    return render(request, 'description.html', context)
