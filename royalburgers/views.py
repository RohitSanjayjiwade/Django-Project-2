from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product, ProductCategory, Modifier, ModifierCategory

# Create your views here.

def index(request):
    categories = ProductCategory.objects.all()
    product = Product.objects.all()
    print(product)
    # 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
    return render(request, "products/index.html", {"product_list": product, "categories_list": categories})



def product_modifiers(request, id):
    product = get_object_or_404(Product, pk=id)
    print("hoooo",product)
    modifiers = product.modifiers.all()
    print("Noooo",modifiers)
    categories = ProductCategory.objects.all()  # Assuming you have a ProductCategory model
    return render(request, "products/modifier.html", {"modifiers": modifiers, "product": product,  "categories": categories})