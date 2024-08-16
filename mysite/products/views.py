from django.shortcuts import get_object_or_404, render
from .models import Product, ProductDetail

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'product_list': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    details = get_object_or_404(ProductDetail, product=product)
    return render(request, 'products_detail.html', {'product': product, 'details': details})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')