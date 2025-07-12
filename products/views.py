from django.shortcuts import render

from .models import Category, Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    roots = categories.filter(parent__isnull=True)
    context = {
        'products': products,
        'categories': categories,
        'roots': roots,
    }
    return render(request, 'products/product_list.html', context)