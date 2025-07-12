from django.shortcuts import render

from .models import Category, Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/product_list.html', context)