from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from core.views import _render
from shop.models import Product
from .cart import Cart
from .forms import CartAddForm


def cart_page(request):
	cart = Cart(request)
	for prod in cart:
		prod['quantity_form'] = CartAddForm(initial={
			'quantity': prod['quantity'],
			'override': True
		})


	return _render(request, 'cart/cart.html', {'cart': cart})


@require_POST
def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	form = CartAddForm(request.POST)
	
	if form.is_valid():
		cd = form.cleaned_data

		cart.add(
			product, 
			quantity=cd['quantity'],
			override_quantity=cd['override']
		)
	return redirect('cart:cart_page')


@require_POST
def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart:cart_page')
