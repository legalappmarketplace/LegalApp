from .forms import ClientRegistrationForm
from .forms import AttorneyRegistrationForm
from .models import Attorney
from .models import Client
from .models import AttroneySpecialities
from .models import Users
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from utils import ATTRONEY_SPECIALITIES
# Create your views here.

class ClientRegistration(CreateView):
    model = Users
    form_class = ClientRegistrationForm
    success_url = '/users/client/register/'
    template_name = 'users/client_registration.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.object = form.save()
        # print(dir(form))
        # print(form.data)
        # print(self.object)
        Client.objects.create(user=self.object)
        return HttpResponseRedirect(self.success_url)

class AttorneyRegistration(CreateView):
        model = Users
        form_class = AttorneyRegistrationForm
        success_url = '/users/attorney/register/'
        template_name = 'users/attorney_registration.html'

        def form_valid(self, form):
            # This method is called when valid form data has been POSTed.
            # It should return an HttpResponse.
            self.object = form.save()
            attroney = Attorney.objects.create(user=self.object)
            specialities = form.data.getlist('speciality')
            for speciality in specialities:
                print(speciality, 'i am here')
                if speciality.lower() in ATTRONEY_SPECIALITIES:
                    print(speciality, 'i am here')
                    AttroneySpecialities.objects.create(speciality=speciality,
                                                      attorney=attroney)
            return HttpResponseRedirect(self.success_url)
