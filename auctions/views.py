from .forms import AttorneyBidForm
from .forms import ClientBidForm
from .models import Bid
from users.models import Attorney
from users.models import Client
from users.models import CustomUser
from cases.models import Case
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormMixin
# Create your views here.

class AttorneyBidView(LoginRequiredMixin, FormMixin, DetailView):
    """Attorney Place Bids"""
    model = Case
    template_name = 'auctions/attorney_bid_form.html'
    form_class = AttorneyBidForm
    success_url = '/'
    login_url = '/users/login/'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, *args, **kwargs):
        client = Case.objects.filter(id=self.kwargs['pk'])[0].client
        buyer = client.user
        bid = Bid(
                    bidder = self.request.user,
                    buyer = buyer,
                    amount = form.data['amount'],
                    client = client,
                    attorney = Attorney.objects.filter(user=self.request.user)[0],
        )
        bid.save()
        return super(AttorneyBidView, self).form_valid(form)

    def render_to_response(self, context):
        attorney = Attorney.objects.filter(user=self.request.user)
        if not attorney:
            return redirect('/')
        return super().render_to_response(context)

class ClientBidView(LoginRequiredMixin, FormMixin, DetailView):
    """Clients Place Counter Bids"""
    model = Case
    template_name = 'auctions/client_bid_form.html'
    form_class = ClientBidForm
    success_url = '/'
    login_url = '/users/login/'

    def render_to_response(self, context):
        client = Client.objects.filter(user=self.request.user)
        if not client:
            return redirect('/')
        return super().render_to_response(context)

    def form_valid(self, form, *args, **kwargs):
        form = self.get_form()
        clientResponse = form.data['bid_responses']
        if clientResponse == 'accept':
            print('client accepted')
        elif clientResponse == 'counteroffer':
            print('client counteroffer')
        elif clientResponse == 'deny':
            print('client deny')

        # client = Case.objects.filter(id=self.kwargs['pk'])[0].client
        # buyer = client.user
        # bid = Bid(
        #             bidder = self.request.user,
        #             buyer = buyer,
        #             amount = form.data['amount'],
        #             client = client,
        #             attorney = Attorney.objects.filter(user=self.request.user)[0],
        # )
        # bid.save()
        # return super(AttorneyBidView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
