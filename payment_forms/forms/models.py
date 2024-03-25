from django.db import models

class Item(models.Model):
    """The Item model"""
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.name

