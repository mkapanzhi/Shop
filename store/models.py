from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default='/defpic.png')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    colors = models.ManyToManyField('ColorProduct')

    def __str__(self):
        return self.name


class ColorProduct(models.Model):
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.color
