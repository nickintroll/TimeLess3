from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from core.views import _render, is_ajax
from .models import Category, Product, OrderItem, Order
from .forms import ProductSearchForm, OrderCreateForm
from cart.forms import CartAddForm
from cart.cart import Cart


def shop_view(request, category_slug=None):
	search_form = ProductSearchForm()

	categories = Category.published.all()
	category = None
	sub_categories = None
	is_search = None

	# category filtering
	if category_slug != None:
		category = get_object_or_404(Category, slug=category_slug)
		sub_categories = category.subcategories.all()
		products = Product.published.all().filter(category__in=[category] + list(category.subcategories.all()))

	else:
		products = Product.published.all()

	# search filtering
	if request.method == 'POST':
		search_form = ProductSearchForm(request.POST)
		if search_form.is_valid():
			cd = search_form.data
			if cd['query'] != '':
				products = Product.published.annotate(
					search=SearchVector('name', 'description')
				)

				if category:
					products = products.filter(search=cd['query'], category__in=[category] + list(category.subcategories.all()))
				else:
					products = products.filter(search=cd['query'])
			
			# filtering by price			
			if cd['price_top'] != '':
				print('TOP')
				print(products)
				products = products.filter(
					price__lte=cd['price_top']
				)
			if cd['price_bot'] != '':
				print('BOT')
				products = products.filter(
					price__gte=cd['price_bot']
				)

			is_search = True

	# PAGINATOR LOGIC
	paginator = Paginator(products, 16)
	page = request.GET.get('page')

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		if is_ajax(request):
			return HttpResponse('')
		products = paginator.page(paginator.num_pages)

	if is_ajax(request):
		return _render(request,'shop/prods_ajax.html', {'products': products})

	return _render(request, 'shop/shop_main.html', \
		{
			'search_form': search_form,
			'is_search': is_search,

			'category': category, 
			'sub_categories': sub_categories, 
			'categories': categories, 
			'products': products
		}
	)


def product_detail(request, product_slug):
	product = get_object_or_404(Product, slug=product_slug)
	add_form = CartAddForm()
	return _render(request, 'shop/product_detail.html', {'product': product, 'add_form': add_form})


def create_order(request):

	trans_dict = {
		'contact_email': 'email',
		'contact_number': 'Phone number'
	}

	cart = Cart(request)
	message = None

	if len(cart) == 0:
		request.session['empty_cart'] = 'YES'
		return redirect('cart:cart_page')

	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			

			for item in cart:
				OrderItem.objects.create(
					order=order,
					product=item['product'],
					price=item['price'],
					quantity=item['quantity']
				)
			cart.clear()

			request.session['complete_order'] = 'YES'
			return redirect('core:main_page')

		field = list(form.errors.keys())[0]
		message = trans_dict[f'{field}']

	else:
		form = OrderCreateForm()


	return _render(request, 'order/create_order.html', {'cart': cart, 'form': form, 'message': message})


def my_order_page(request):
	results = False
	orders = None
	form = OrderCreateForm()
	
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			results = True
			orders = Order.objects.all().filter(contact_number=cd['contact_number'], contact_email=cd['contact_email'])
	
	return _render(request, 'order/my_order.html', {'orders': orders, 'form': form, 'results': results})
