from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(Brand)
class InHouseProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'unit_price', 'total_quantity')  # Customize the displayed columns in the list view

    fieldsets = (
        ('General Information', {
            'fields': ('name', 'description', 'product_type', 'category', 'sku', 'unit', 'color', 'unit_price', 'purchase_price')
        }),
        ('Pricing and Discounts', {
            'fields': ('tax', 'discount', 'discount_type', 'shipping_cost')
        }),
        ('Inventory', {
            'fields': ('total_quantity', 'minimum_order_quantity')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_image')
        }),
        ('Images', {
            'fields': ('product_images', 'product_thumbnail')
        }),
    )

admin.site.register(InHouseProducts, InHouseProductsAdmin)