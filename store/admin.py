from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'updated_at',]
    search_fields = ['name',]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'stock']
    list_filter = ['title', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
