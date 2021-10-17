from django.db import models

class Producto(models.Model):
    name = models.CharField(max_length=20)
    stock = models.IntegerField(blank=False)

def __str__(self):
    return self.name
