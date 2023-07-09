from django.contrib import admin

from config.product.models import Category, Brand, Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
