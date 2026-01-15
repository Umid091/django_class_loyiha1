from django.db import models
from django.forms.fields import CharField


class Book(models.Model):
    name=models.CharField(max_length=20)
    maker=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    author=models.CharField(max_length=20)
    desc=models.TextField(blank=True, null=True)
    isbn=models.IntegerField()

    def __str__(self):
        return f'{self.name} | {self.author}'



class Car(models.Model):
    name=models.CharField(max_length=30)
    color=models,CharField(max_length=40)
    raqam=models.IntegerField(max_length=50)
    year=models.DateField(max_length=30)
    create_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} "





# Create your models here.
