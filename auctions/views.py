from .forms import AttorneyBidForm
from .models import Bid
from users.models import Attorney
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
    template_name = 'auctions/bid_form.html'
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
        if not attorney.exists():
            return redirect('/')
        return super().render_to_response(context)
