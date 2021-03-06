from .forms import UserRegistrationForm
from .forms import AttorneyRegistrationForm
from .models import Attorney
from .models import Client
from .models import AttroneySpecialities
from .models import CustomUser
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.utils.decorators import method_decorator
from utils import ATTRONEY_SPECIALITIES
from django.contrib.auth.hashers import make_password

# Create your views here.

class ClientRegistration(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    success_url = '/users/login'
    template_name = 'users/client_registration.html'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.object = form.save()
        self.object.set_password(self.object.password)
        self.object.save()
        # print(dir(form))
        # print(form.data)
        # print(self.object)
        Client.objects.create(user=self.object)
        return HttpResponseRedirect(self.success_url)

class AttorneyRegistration(CreateView):
        model = CustomUser
        form_class = AttorneyRegistrationForm
        success_url = '/users/login'
        template_name = 'users/attorney_registration.html'

        def form_valid(self, form):
            # This method is called when valid form data has been POSTed.
            # It should return an HttpResponse.
            self.object = form.save()
            self.object.set_password(self.object.password)
            self.object.save()
            attroney = Attorney.objects.create(user=self.object)
            specialities = form.data.getlist('speciality')
            for speciality in specialities:
                print(speciality, 'i am here')
                if speciality.lower() in ATTRONEY_SPECIALITIES:
                    print(speciality, 'i am here')
                    AttroneySpecialities.objects.create(speciality=speciality,
                                                      attorney=attroney)
            return HttpResponseRedirect(self.success_url)

class UserLogin(FormView):
    form_class = AuthenticationForm
    template_name = 'users/client_login.html'
    success_url = '/'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()
        return super(UserLogin, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(UserLogin, self).form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url # return next url for redirection
        return self.success_url # return some other url if next parameter not present

    def render_to_response(self, context):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().render_to_response(context)

class UserLogout(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(UserLogout, self).get(request, *args, **kwargs)
