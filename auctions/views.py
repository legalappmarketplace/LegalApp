from .forms import AttorneyBidForm
from .models import Bid
from cases.models import Case
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormMixin
# Create your views here.

class AttorneyBidView(LoginRequiredMixin, FormMixin, DetailView):
    """Attorney Place Bids"""
    model = Case
    template_name = 'auctions/bid_form.html'
    form_class = AttorneyBidForm
    success_url = '/'
    login_url = '/users/login/'
