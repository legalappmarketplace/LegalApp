# some_app/views.py
from django.shortcuts import redirect
from django.views.generic import TemplateView
from users.models import Attorney
from users.models import Client

class HomeView(TemplateView):
    template_name = "home.html"

    def render_to_response(self, context):
        user = self.request.user
        if self.request.user.is_authenticated:
            client = Client.objects.filter(user=user)
            attorney = Attorney.objects.filter(user=user)
            if attorney.exists():
                return redirect('/cases/list/')
            if client.exists():
                return redirect('/cases/user/cases')
        return super().render_to_response(context)
