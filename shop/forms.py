from django import forms
from . import models


class ProductSearchForm(forms.Form):
	query = forms.CharField(max_length=200, required=False,
		widget = forms.TextInput(attrs={'placeholder':'Search request'})
	)
	price_top = forms.IntegerField(required=False,
		widget = forms.TextInput(attrs={'placeholder':'max price', 'type': 'number'})
	)
	price_bot = forms.IntegerField(required=False,
		widget = forms.TextInput(attrs={'placeholder':'min price', 'type': 'number'})
	)

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = models.Order
		fields = ['contacts', ]