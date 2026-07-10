from django.db import models
from django.conf import settings


# Create your models here.
from menu.models import MenuItem,Drink


class Order(models.Model):
    STATUS=[
        ('pending','Pending'),
        ('preparing','Preparing'),
        ('served','Served'),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='orders_placed'
    )
    taken_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='orders_handled'
    )


    created_at=models.DateTimeField(auto_now_add=True)
    total_cost=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status=models.CharField(max_length=20,choices=STATUS,default='pending')

    def __str__(self):
        return f'Order {self.id} - {self.status}'
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    menu_item=models.ForeignKey(MenuItem,on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField(default=1)
    price_at_time_of_order=models.DecimalField(max_digits=10,decimal_places=2)


class OrderDrink(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='drinks')
    drink=models.ForeignKey(Drink,on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField(default=1)
    price_at_time_of_order=models.DecimalField(max_digits=10,decimal_places=2)

