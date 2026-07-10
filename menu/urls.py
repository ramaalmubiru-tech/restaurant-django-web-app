from django.urls import path
from . import views
app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('add/food/<int:item_id>/', views.add_to_cart,name='add_to_cart'),
    path('add/drink/<int:item_id>/', views.add_drink_to_cart,name='add_drink_to_cart'),
]
