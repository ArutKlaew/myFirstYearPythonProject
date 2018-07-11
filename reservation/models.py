from django.db import models
from django.contrib.auth.models import User

class ReservationData(models.Model):
    seat = models.PositiveIntegerField(default=1)
    reserved_time = models.DateTimeField('reserved_time',help_text="Please fill in YYYY-MM-DD HH:MM format")
    reserved_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('reserved_time',)

    def __str__(self):
        return "Reserve by :" + self.reserved_by.username


class Menu(models.Model):
    name = models.CharField(max_length=120, db_index=True,unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class OrderMenu(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    menu_name = models.ForeignKey(Menu,on_delete=models.CASCADE)
    reservation = models.ForeignKey(ReservationData, on_delete=models.CASCADE)

    def __str__(self):
        return ("Ordered By : %s\nMenu : %s\nQuantity : %d\n" %(self.reservation.reserved_by.username,self.menu_name.name,self.quantity))

    def get_cost(self):
        return self.menu_name.price * self.quantity
