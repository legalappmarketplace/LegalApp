from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class CaseCreateView(CreateView):
    model = Product
    template_name = 'cases/case_form.html'
    form_class = ProductModelForm
    success_url = '/list'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(CaseCreateView, self).form_valid(form)
