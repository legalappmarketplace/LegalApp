from .models import Bid
from django import forms
from utils import BID_RESPONSES

PUBLISH_CHOICES = tuple((response.lower(), response.title()) for response in
                    BID_RESPONSES)

class AttorneyBidForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
    bid_responses = forms.ChoiceField(
        required=True,
        widget=forms.Select(),
        choices=PUBLISH_CHOICES,
    )
    class Meta:
        model = Bid
        exclude = ('previousBid', 'counterBid', 'bidAccepted', 'attorney',
                   'client', 'buyer', 'bidder', 'case')

class ClientBidForm(AttorneyBidForm):
    """Client Bid Form"""
