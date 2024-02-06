from django.db import models
from django.contrib.auth.models import User
# Create your models here

class Gun(models.Model):
    name = models.CharField(max_length=40)
    category= models.CharField(max_length=30)
    price = models.IntegerField()
    caliber = models.FloatField()
    producer= models.CharField(max_length=40)
    description = models.TextField(max_length=400, null=True, blank=True)
    image = models.ImageField(upload_to='gun_images/',  null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guns = models.ManyToManyField(Gun, through='OrderGun')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField(max_length=200)

    def calculate_total_price(self):
        total_price = sum(order_gun.gun.price * order_gun.quantity for order_gun in self.ordergun_set.all())
        return round(total_price, 2)

    def save(self, *args, **kwargs):
        # Save the order to generate a primary key
        super().save(*args, **kwargs)

        # Now save the related OrderGun instances
        for order_gun in self.ordergun_set.all():
            order_gun.save()

        # Update the total price after saving related OrderGun instances
        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)

class OrderGun(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    gun = models.ForeignKey(Gun, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)