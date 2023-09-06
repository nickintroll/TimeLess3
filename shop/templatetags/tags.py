from django import template
from shop.models import ProductParameter, Product
register = template.Library()

@register.filter
def get_analogs(parameter, product):
	analogs = ProductParameter.objects.all().filter(name=parameter.name, product__name=product.name)
	analogs = [{'parameter': i, 'product': i.product.all()[0]} for i in analogs]
	return analogs