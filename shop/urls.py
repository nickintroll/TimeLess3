from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
	path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
	path('<slug:category_slug>/', views.shop_main, name='category'),
	path('', views.shop_main, name='shop_main'),


]