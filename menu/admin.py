from django.contrib import admin
from .models import Category,MenuItem,DrinkType,Drink

# Register your models here.
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(DrinkType)
admin.site.register(Drink)