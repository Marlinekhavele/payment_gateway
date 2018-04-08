from django.db import models
import datetime
from django.contrib.auth.models import User as MainUser

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName
 
class Product(models.Model):
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productBrand = models.CharField(max_length=100)


class Payment(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    amount = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.user.username




class User(models.Model):
    name =models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    amount = models.IntegerField()
    product = models.TextField()
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
     transaction_Id=models.IntegerField()
     sender_number =models.IntegerField()
     receiver_number=models.IntegerField()
     amount=models.IntegerField()
     transaction_date=models.DateTimeField(default=datetime.date.today())



     def __str__(self):
         return self.transaction_Id

