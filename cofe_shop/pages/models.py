from django.db import models

# Create your models here.

class Sarlavha(models.Model):
    cafe_name = models.CharField(max_length=30)
    bio =  models.CharField(max_length=15)
    about = models.CharField(max_length=200)
    def __str__(self):
        return self.cafe_name
    
class Menu(models.Model):
    cofee_name = models.CharField(max_length=25)
    big_price = models.PositiveIntegerField(default=0)
    small_price = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cofee_name
    

class Contact(models.Model):
    name = models.CharField(max_length=22)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email


