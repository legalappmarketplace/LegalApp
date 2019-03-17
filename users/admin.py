from django.contrib import admin
from .models import Attorney
from .models import AttroneySpecialities
from .models import Client
from .models import Users
# Register your models here.

admin.site.register(Attorney)
admin.site.register(AttroneySpecialities)
admin.site.register(Client)
admin.site.register(Users)
