from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Stock(models.Model):
    productid=models.CharField(max_length=120,unique=True)
    productname=models.CharField(max_length=120,unique=True)
    quantity=models.PositiveIntegerField(default=0)
    stock_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.productname

    options = (
        ("available", "available"),
        ("out of stock", "out of stock"),
        ("active", "active"),
        ("inactive", "inactive")
    )
    status = models.CharField(max_length=120, choices=options, default="available")
