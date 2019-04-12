from .forms import CaseForm
from users.models import Attorney
from users.models import AttroneySpecialities
from users.models import CustomUser
from .models import Case
from .models import Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
# Create your views here.

class CaseCreateView(LoginRequiredMixin, CreateView):
    model = Case
    template_name = 'cases/create_case_form.html'
    form_class = CaseForm
    success_url = '/cases/user/cases'
    login_url = '/users/login/'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        if user.is_authenticated:
            self.object = form.save()
            user = CustomUser.objects.filter(email=user)[0]
            client = Client.objects.filter(user=user)[0]
            print(user, client)
            self.object.client = client
            self.object.save()
        return super(CaseCreateView, self).form_valid(form)


class CaseListView(LoginRequiredMixin, ListView):
    model = Case
    template_name = 'cases/list_view.html'
    context_object_name = 'cases'
    queryset = Case.objects.all()
    login_url = '/users/login/'

    def get_queryset(self):
        attorney = Attorney.objects.filter(user=self.request.user)
        if attorney.exists():
            attorney = attorney[0]
            attroney_interest_queryset = AttroneySpecialities.objects.filter(
                                                           attorney=attorney.id)
            interest = [attrone_speciality_object.speciality for
                                    attrone_speciality_object in
                                    attroney_interest_queryset ]
            relevant_cases = []
            for case in Case.objects.all():
                if case.caseType1 in interest or case.caseType2 in interest or \
                        case.caseType3 in interest:
                        relevant_cases.append(case)
            return relevant_cases
        return []

    def render_to_response(self, context):
        attorney = Attorney.objects.filter(user=self.request.user)
        if not attorney.exists():
            return redirect('/')
        return super().render_to_response(context)

class CaseDetailView(LoginRequiredMixin, DetailView):
    model = Case

class UsersCases(LoginRequiredMixin, ListView):
        model = Case
        template_name = 'cases/user_cases_list_view.html'
        context_object_name = 'cases'
        login_url = '/users/login/'

        def get_queryset(self):
            client = Client.objects.filter(user=self.request.user)
            if client.exists():
                client = client[0]
                return Case.objects.filter(client=client)
            return []

        def render_to_response(self, context):
            client = Client.objects.filter(user=self.request.user)
            if not client.exists():
                return redirect('/')
            return super().render_to_response(context)
