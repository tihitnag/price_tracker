from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView

from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    
class ProductAddView(CreateView):
    model = Product
    template_name = "products/add_product.html"
    form_class = ProductForm
    # fields = ['name', 'url']
    success_url = reverse_lazy('product-list')
    
    
