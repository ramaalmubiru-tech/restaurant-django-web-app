from django.shortcuts import render
from .models import Category, MenuItem, DrinkType, Drink
# Create your views here.

def menu_list(request):
    categories= Category.objects.prefetch_related('menuitem_set').all()
    drink_types=DrinkType.objects.prefetch_related('drink_set').all()


    context={
        'categories': categories,
        'drink_types': drink_types,
    }
    return render(request, 'menu/menu_list.html', context)

