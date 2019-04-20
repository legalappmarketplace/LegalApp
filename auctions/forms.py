from .models import Bid
from django import forms

class AttorneyBidForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
    class Meta:
        model = Bid
        exclude = ('previousBid', 'counterBid', 'bidAccepted', 'attorney',
                   'client', 'buyer', 'bidder', 'case')

class ClientBidForm(AttorneyBidForm):
    """Client Bid Form"""
