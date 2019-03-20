from django.contrib import admin
from .models import Case
# Register your models here.
class CaseAdmin(Case):
    list_display = ['id', 'pk', 'caseType1']
admin.site.register(Case)
