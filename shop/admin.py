from django.contrib import admin
from .models import (Category, SubCategory, Product)

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name', )}
	
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name', )}
	list_filter = ['category', ]

@admin.register(Product)
class Product(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
	list_filter = ['available', 'sub_category', 'created', 'updated']
	list_editable = ['available', 'price']
	prepopulated_fields = {'slug': ('name', )}
	