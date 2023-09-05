from django.shortcuts import render, get_object_or_404
from core.views import _render
from .models import Product, Category
from .forms import ShopSearchForm


def shop_main(request, category_slug=None):
	# search_form = ProductSearchForm()

	categories = Category.published.all()
	category = None
	sub_categories = None

	search_form = ShopSearchForm()

	# category filtering
	if category_slug != None:
		category = get_object_or_404(Category, slug=category_slug)
		sub_categories = category.subcategories.all()
		products = Product.published.all().filter(category__in=[category] + list(category.subcategories.all()))

	else:
		products = Product.published.all()

	# search filtering
	# if request.method == 'POST':
		# search_form = ProductSearchForm(request.POST)
		# if search_form.is_valid():
			# cd = search_form.data

	return _render(request, 'shop/main.html',
		{
			'search_form': search_form,

			'category': category, 
			'sub_categories': sub_categories, 
			'categories': categories, 
			'products': products
		}
	)


def product_detail(request, product_slug):
	product = get_object_or_404(Product, slug=product_slug)
	# add_form = CartAddForm()
	return _render(
		request, 
		'shop/product_detail.html', 
		{
			'product': product, 
			# 'add_form': add_form
		}
		)
