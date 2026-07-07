from django.urls import path
from . import views

app_name= 'orders'

urlpatterns = [
    #path('place/',views.place_order,name='place_order'),
    #path('confirm/',views.confirm_order,name='confirm_order'),
    #path('receipt/<int:order_id>/',views.receipt,name='receipt'),
    path('',views.view_cart,name='view_cart')
]