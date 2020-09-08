from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product

    def get_queryset(self):
        return Product.objects.all()
