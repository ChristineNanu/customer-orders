from customers.models import Customer
from django.db import models


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(
        Customer, related_name="orders", on_delete=models.CASCADE
    )
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for {self.customer.name}"
