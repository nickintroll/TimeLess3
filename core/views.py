from django.shortcuts import render
from shop.models import Category, Product


def _render(request, template, data):
	data['all_categories'] = Category.published.all().filter(special=True)
	return render(request, template, data)


# Create your views here.
def main_page(request):
	products = Product.published.all().filter(special=True)
	order_notification = None

	if 'complete_order' in request.session.keys():
		del request.session['complete_order']
		order_notification = 'yes'
	return _render(request, 'core/main_page.html', {'products': products, 'order_notification': order_notification})
