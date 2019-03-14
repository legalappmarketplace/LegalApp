from django.contrib import admin
from django.urls import path
from .views import CaseCreateView

urlpatterns = [
    path('upload/', CaseCreateView.as_view(), name='case_create_view'),
]
