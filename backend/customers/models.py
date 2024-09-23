from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
