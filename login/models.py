from django.db import models

# Create your models here.
class Credentials(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=10)
    def __str__(self):
        return f'{self.Username}, {self.Password}'

class Cred(models.Model):
    Name=models.CharField(max_length=10)
    Age=models.CharField(max_length=2)
    def __str__(self) -> str:
        return f'{self.Name},{self.Age}'   



class Product(models.Model):
    productName=models.CharField(max_length=200)
    productCategory=models.CharField(max_length=200)
    productWarranty=models.CharField(max_length=200)
    productPrice=models.FloatField(max_length=30)
    productBrand=models.CharField(max_length=100)

    def __str__(self)->str:
        return f'{self.productName} {self.productCategory} {self.productPrice} {self.productBrand} {self.productWarranty}'

class CustomerDetails(models.Model):
    CName=models.CharField(max_length=30)
    Cid=models.IntegerField()
    Cage=models.IntegerField()
    CmailId=models.CharField(max_length=50)
    def __str__(self)->str:
        return f'{self.CName} {self.Cid} {self.Cage} {self.CmailId}'





 

''' db -table: cred:
initially: 1 (pk_id)
5 data / rows /records  [id: 1,2,3,4,5]
[1,2,4,5]
new data inserted  id:6

1. 100 [60-80] id also removed  // 
1... 100 []truncation to be processed to have pk_id start pointer as 1 '''
