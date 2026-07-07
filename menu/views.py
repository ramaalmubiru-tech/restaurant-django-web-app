from django.shortcuts import render,redirect
from .models import Category, MenuItem, DrinkType, Drink
# Create your views here.

def menu_list(request):
    #fetch
    categories= Category.objects.prefetch_related('menuitem_set').all()
    drink_types=DrinkType.objects.prefetch_related('drink_set').all()

    #package

    context={
        'categories': categories,
        'drink_types': drink_types,
    }

    #return response
    return render(request, 'menu/menu_list.html', context)
def add_to_cart(request,item_id):
    cart=request.session.get('cart',{})
    item=MenuItem.objects.get(id=item_id)
    if str(item_id) not in cart:
        cart[str(item_id)]={
            'name':item.name,
            'price':str(item.price),
            'quantity':1,
        }
    else:
        cart[str(item_id)]['quantity']+=1

    request.session['cart']=cart
    request.session.modified=True
    return redirect('menu:menu_list')