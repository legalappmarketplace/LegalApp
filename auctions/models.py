from django.db import models
from cases.models import Case
from users.models import Attorney
from users.models import Client
from users.models import CustomUser
# Create your models here.

class Bid(models.Model):
    "Represent Bids"
    bidder = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name='bidder')
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                              related_name='buyer')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE)
    counterBid = models.BooleanField(null=True)
    previousBid = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    bidAccepted = models.BooleanField(null=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
