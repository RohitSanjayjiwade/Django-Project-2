from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    # Add any other fields relevant to your product category

    def __str__(self):
        return self.name


class Modifier(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='royalburgers/static/images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class ModifierCategory(models.Model):
    name = models.CharField(max_length=255)
    modifiers = models.ManyToManyField(Modifier, blank=True)
    # Add any other fields relevant to your modifier category

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='royalburgers/static/images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    modifiers = models.ManyToManyField(ModifierCategory, blank=True)
    sides = models.ManyToManyField('self', blank=True, symmetrical=False)


    def __str__(self):
        return self.title
