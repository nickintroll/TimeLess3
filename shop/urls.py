from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
	path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
	path('<slug:category_slug>/', views.shop_view, name='category'),
	path('', views.shop_view, name='shop_main'),
    ]
