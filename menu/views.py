from django.shortcuts import render,redirect
from .models import Category, MenuItem, DrinkType, Drink
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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
    if 'food_' + str(item_id) not in cart:
        cart['food_' + str(item_id)]={
            'name':item.name,
            'price':str(item.price),
            'quantity':1,
        }
    else:
        cart['food_' + str(item_id)]['quantity']+=1

    request.session['cart']=cart
    request.session.modified=True
    return redirect('menu:menu_list')
def add_drink_to_cart(request,item_id):
    cart=request.session.get('cart',{})
    item=Drink.objects.get(id=item_id)
    if 'drink_' + str(item_id) not in cart:
        cart['drink_' + str(item_id)]={
            'name':item.name,
            'price':str(item.price),
            'quantity':1,
        }
    else:
        cart['drink_' + str(item_id)]['quantity']+=1

    request.session['cart']=cart
    request.session.modified=True
    return redirect('menu:menu_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu:menu_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})










