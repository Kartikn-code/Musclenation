from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200) 
    age=models.CharField(max_length=250)
    def __str__(self):
        return f'{self.name}, {self.age}'

class Customer1(models.Model):
    name=models.CharField(max_length=200) 
    age=models.CharField(max_length=250)
    def __str__(self):
        return f'{self.name}, {self.age}'

