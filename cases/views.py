from .forms import CaseForm
from .models import Case
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
# Create your views here.

class CaseCreateView(CreateView):
    model = Case
    template_name = 'cases/create_case_form.html'
    form_class = CaseForm
    success_url = '/cases/upload'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(CaseCreateView, self).form_valid(form)

# ogin_required(login_url='users/login/')
class CaseListView(LoginRequiredMixin, ListView):
    model = Case
    template_name = 'cases/list_view.html'
    context_object_name = 'cases'
    queryset = Case.objects.all()
    login_url = '/users/login/'
