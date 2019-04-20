from django import template
from auctions.models import Bid
from cases.models import Case
from users.models import Attorney

register = template.Library()

@register.filter(name='bidPrice')
def bidPrice(caseID):
    pendingBid = Bid.objects.filter(case=caseID)[0]
    if pendingBid:
        return pendingBid.amount
    return None

@register.filter(name='findPendingBids')
def findPendingBids(caseID):
    pendingBid = Bid.objects.filter(case=caseID)
    if pendingBid:
        return pendingBid[0]
    return None

@register.filter(name='getAttorney')
def getAttorneyName(caseID):
    bid = Bid.objects.filter(case=caseID)
    if bid:
        attorneyName = bid[0].attorney.user.username
        return attorneyName
    return None

register.filter('bidPrice', bidPrice)
register.filter('findPendingBids', findPendingBids)
register.filter('getAttorneyName', getAttorneyName)
