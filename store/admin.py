from django.contrib import admin

from store.models import Product, Store, ColorProduct

# Register your models here.
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(ColorProduct)
