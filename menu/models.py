from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    is_available=models.BooleanField(db_default=True)
    requires_quantity=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class DrinkType(models.Model):
    name=models.CharField(max_length=100)

class Drink(models.Model):
    drink_type=models.ForeignKey(DrinkType,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    