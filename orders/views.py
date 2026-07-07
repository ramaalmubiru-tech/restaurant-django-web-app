from django.shortcuts import render

# Create your views here.
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