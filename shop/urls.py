from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
	path('my_order/', views.my_order_page, name='my_order'),
	path('order/', views.create_order, name='create_order'),
	path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
	path('<slug:category_slug>/', views.shop_view, name='category'),
	path('', views.shop_view, name='shop_main'),
    ]
