from django.db import models
from users.models import Attorney
from users.models import Client
# Create your models here.

class Case(models.Model):
    """ Represents Users Cases"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    attorney =  models.ForeignKey(Attorney, on_delete=models.CASCADE,
                                    null=True)
    caseType1 = models.CharField(max_length=250)
    caseType2 = models.CharField(max_length=250)
    caseType3 = models.CharField(max_length=250)
    description = models.TextField()
