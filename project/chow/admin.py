from django.contrib import admin
from chow.models import Product,Menu,CustomFoods1
from atexit import register

# Register your models here.
admin.site.register(Menu)
admin.site.register(Product)
admin.site.register(CustomFoods1)