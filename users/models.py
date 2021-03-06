from utils import PASSWORD_ERROR_MESSAGES
from utils import EMAIL_ERROR_MESSAGES
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    password = models.CharField(max_length=500, unique=True,
                                           error_messages=PASSWORD_ERROR_MESSAGES)
    firstName = models.CharField(max_length=500, null=True)
    lastName = models.CharField(max_length=500, null=True)
    email = models.EmailField(unique=True, error_messages=EMAIL_ERROR_MESSAGES)
    birthDate = models.DateField(null=True)
    username = models.CharField(max_length=500, unique=True)
    about = models.TextField(null=True)

    def __str__(self):
        return self.email

class Attorney(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

class Client(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

class AttroneySpecialities(models.Model):
    attorney = models.ForeignKey('Attorney', on_delete=models.CASCADE)
    speciality = models.CharField(max_length=500)
