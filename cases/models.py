from django.db import models
from .users.models import Attorney
from .users.models import Client
# Create your models here.

class Case(models.Model):
    """ Represents Users Cases"""
    clientID = models.ForeignKey('Client', on_delete=models.CASCADE)
    attorneyID =  models.ForeignKey('Attorney', on_delete=models.CASCADE,
                                    null=True)
    description = models.TextField()
