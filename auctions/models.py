from django.db import models
from users.models import Attorney
from users.models import Client
from users.models import CustomUser
# Create your models here.

class Bids(models.Model):
    "Represent Bids"
    bidder = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name='bidder')
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                              related_name='buyer')
    amount = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE)
    counterBid = models.BooleanField()
    previousBid = models.ForeignKey('self', on_delete=models.CASCADE)
