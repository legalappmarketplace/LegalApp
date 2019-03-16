from django.contrib import admin
from .models import Attorney
from .models import Client
# Register your models here.

admin.site.register(Attorney)
admin.site.register(Client)
