from django import forms

class ProductSearchForm(forms.Form):
	name = forms.CharField(max_length=200)
