from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    firstName = models.CharField(max_length=500)
    lastName = models.CharField(max_length=500)
    email = models.EmailField()
    birthDate = models.DateField()

class Attorney(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

class Client(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
