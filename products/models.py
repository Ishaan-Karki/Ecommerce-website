from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    digital = models.BooleanField(default=False)
    image = models.ImageField(null = True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def get_add_to_cart_url(self):
        return reverse("add-to-cart")


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.order_item_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.order_item_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    



class Order_item(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def add_to_cart(self):
        orderitems = self.order_item_set.all()
        if orderitems in Order:
            self.quantity += 1
        else:
            self.product += 1
            

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    zipcode = models.CharField(max_length=256)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

