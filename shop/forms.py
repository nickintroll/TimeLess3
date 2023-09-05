from django import forms

class ShopSearchForm(forms.Form):
	query = forms.CharField(
		max_length=80, 
		widget=forms.TextInput(attrs={'placeholder': 'search'})
		)
