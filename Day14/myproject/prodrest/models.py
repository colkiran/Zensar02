from django.db import models

# Create your models here.
class Product(models.Model):
    prodname = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()

    def __str__(self):
        return self.prodname

