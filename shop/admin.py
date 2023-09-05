from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'parent_category', 'special')
	list_filter = ['special', 'parent_category']
	prepopulated_fields = (
		{'slug': ('parent_category', 'name')}
	)

class ImageProductInline(admin.TabularInline):
	model = models.Image
	raw_id_fields = ['product']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'category', 'special')
	list_filter = ['special', 'category']
	prepopulated_fields = (
		{'slug': ('name', )}
	)
	inlines = [ImageProductInline]



class OrderItemInline(admin.TabularInline):
	model = models.OrderItem
	raw_id_fields = ['product']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'created', 'status']
	list_filter = ['status']
	inlines = [OrderItemInline]


