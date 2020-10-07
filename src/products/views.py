from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product


# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def product_list_view(request):
    queryset = Product.objects.all()
    template = 'products/product_list.html'
    context = {
        'object_list': queryset,
    }
    return render(request, template_name=template, context=context)


class ProductDetailView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def product_detail_view(request, pk):
    instance = get_object_or_404(Product, pk=pk)
    template = 'products/product_details.html'
    context = {
        'object': instance,
    }
    return render(request, template_name=template, context=context)
