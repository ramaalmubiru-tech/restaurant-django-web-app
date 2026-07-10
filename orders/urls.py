from django.urls import path
from . import views
app_name= 'orders'

urlpatterns = [
    #path('place/',views.place_order,name='place_order'),
    path('confirm/',views.confirm_order,name='confirm_order'),
    path('receipt/<int:order_id>/',views.receipt,name='receipt'),
    path('',views.view_cart,name='view_cart'),
    path('staff/', views.staff_dashboard, name='staff_dashboard'),
path('staff/update/<int:order_id>/',
     views.update_order_status,
     name='update_status'),

]