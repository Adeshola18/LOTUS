from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'total_products', 'total_amount',]
    list_filter = ['title']


admin.site.register(Order, OrderAdmin)
