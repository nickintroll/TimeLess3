from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent_category')
    prepopulated_fields = (
        {'slug': ('parent_category', 'name')}
    )

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category')
    prepopulated_fields = (
        {'slug': ('name', )}
    )

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'file', 'is_primary')
