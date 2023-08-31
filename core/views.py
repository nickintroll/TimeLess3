from django.shortcuts import render
from shop.models import Category, Product


def _render(request, template, data):
	data['all_categories'] = Category.published.all()
	return render(request, template, data)


# Create your views here.
def main_page(request):
	products = Product.published.all()
	return _render(request, 'core/main_page.html', {'products': products})
