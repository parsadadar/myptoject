from django.contrib import admin
from .models import products, category, subcategory

# Register your models here.


admin.site.register(products)
admin.site.register(category)
admin.site.register(subcategory)