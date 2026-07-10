from django.shortcuts import render , redirect
from .models import Order, OrderItem,OrderDrink
from menu.models import MenuItem,Drink,DrinkType
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def staff_dashboard(request):
    orders = Order.objects.filter(
        status__in=['pending', 'preparing']
    ).order_by('-created_at')
    return render(request,
                  'orders/staff_dashboard.html',
                  {'orders': orders})

@staff_member_required
def update_order_status(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(id=order_id)
        order.status = request.POST.get('status')
        order.save()
    return redirect('orders:staff_dashboard')

# Create your views here.
@login_required
def view_cart(request):
    cart=request.session.get('cart',{})
    total=0
    
    for item in cart.values():
        items_cost=float(item['price']) * item['quantity']
        item['items_total_cost']=items_cost
        total+=items_cost
    context={
        'cart':cart,
        'total':total,
    }
    return render(request, 'orders/cart.html', context)
@login_required
def confirm_order(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        
        # Step 1: Calculate total
        total = sum(
            float(item['price']) * item['quantity'] 
            for item in cart.values()
        )
        
        # Step 2: Create the Order row
        order = Order.objects.create(
            customer=request.user,
            total_cost=total,
            status='pending'
        )
        
        # Step 3: Create one OrderItem per cart item
        for item_id, item in cart.items():
            if item_id.startswith('food_'):
                real_id=int(item_id.split('_')[1])
                menu_item = MenuItem.objects.get(id=real_id)

                OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=item['quantity'],
                price_at_time_of_order=item['price'],
            )
            else:
                real_id=int(item_id.split('_')[1])
                drinkitem=Drink.objects.get(id=real_id)
                OrderDrink.objects.create(
                    order=order,
                    drink=drinkitem,
                    quantity=item['quantity'],
                    price_at_time_of_order=item['price'],
                )


        
        # Step 4: Clear the cart
        del request.session['cart']
        request.session.modified = True
        
        # Step 5: Redirect to receipt
        return redirect('orders:receipt', order_id=order.id)
    
    return redirect('menu:menu_list')

@login_required
def receipt(request, order_id):
    order = Order.objects.get(id=order_id)
    items = order.items.all()
    drinks = order.drinks.all()
    
    context = {
        'order': order,
        'items': items,
        'drinks': drinks,
    }
    return render(request, 'orders/receipt.html', context)