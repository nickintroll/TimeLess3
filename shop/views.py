from django.shortcuts import render, get_object_or_404

from core.views import _render
from .models import Category, Product


def category_view(request, category_slug):
	category = get_object_or_404(Category, slug=category_slug)
	return _render(request, 'shop/category_page.html', {'category': category})


def product_detail(request, product_slug):
	product = get_object_or_404(Product, slug=product_slug)
	return _render(request, 'shop/product_detail.html', {'product': product})