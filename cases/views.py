from .forms import CaseForm
from .models import Case
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

# Create your views here.

class CaseCreateView(CreateView):
    model = Case
    template_name = 'cases/create_case_form.html'
    form_class = CaseForm
    success_url = '/cases/upload'

    # def form_valid(self, form):
    #     user = self.request.user
    #     form.instance.user = user
    #     return super(CaseCreateView, self).form_valid(form)
