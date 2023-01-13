from django.contrib import admin
from .models import Product,Order


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity')
    list_filter=['category']

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.site_header='Bisiventory'

admin.site.register(Order)