from django.http import Http404
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

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()



def product_list_view(request):
    queryset = Product.objects.all()
    template = 'products/product_list.html'
    context = {
        'object_list': queryset,
    }
    return render(request, template_name=template, context=context)


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/product_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(id=pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(id=pk)


def product_detail_view(request, pk, *args, **kwargs):
    # instance = get_object_or_404(Product, pk=pk)
    instance = Product.objects.get_by_id(id=pk)
    # print(instance)
    if instance is None:
        raise Http404("Product doesn't exist")
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() ==1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

    template = 'products/product_details.html'
    context = {
        'object': instance,
    }
    return render(request, template_name=template, context=context)
