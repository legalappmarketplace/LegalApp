from .forms import RegisterForm
from .models import Attorney
from .models import Client
from .models import Users
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView

# Create your views here.

class UserRegistration(CreateView):
    model = Users
    form_class = RegisterForm
    success_url = '/users/register'
    template_name = 'users/registration.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.object = form.save()
        # print(dir(form))
        # print(form.data)
        # print(self.object)
        if form.data['userType'] == 'attorney':
            Attorney.objects.create(user=self.object)
        else:
            Client.objects.create(user=self.object)
        return HttpResponseRedirect(self.success_url)
