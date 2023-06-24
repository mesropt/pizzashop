from django.db import models

from helpers.choices import DoughTypeChoices
from helpers.upload_files import upload_pizza_image


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
    def __str__(self):
        return self.name

class Pizza(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='pizza')
    name = models.CharField(max_length=255)
    dough_type = models.CharField(max_length=10, choices=DoughTypeChoices.choices)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_pizza_image)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
