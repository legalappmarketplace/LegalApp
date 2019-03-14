from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField()
    password = models.CharField()
    firstName = models.CharField()
    lastName = models.CharField()
    birthDate = models.DateField()

class Attorney(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

class Client(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
