from django.shortcuts import render

def _render(request, template, context):
	# do stuff
	return render(request, template, context)

def main_page(request):

	return _render(request, 'main/main.html', {})
