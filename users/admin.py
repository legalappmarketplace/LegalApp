from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Attorney
from .models import AttroneySpecialities
from .models import Client
from .models import CustomUser
# Register your models here.
from .forms import UserRegistrationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Attorney)
admin.site.register(AttroneySpecialities)
admin.site.register(Client)
