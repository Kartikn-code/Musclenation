from django.db import models

# Create your models here.
class Gymblog(models.Model):
    Title=models.CharField(max_length=200)
    Description=models.CharField(max_length=300)
    def __str__(self):
         return f'{self.Title}, {self.Description}'