from django.contrib import admin
from django.urls import path
from .views import UserRegistration

urlpatterns = [
    # path('login/', CaseCreateView.as_view(), name='case_create_view'),
    path('register/', UserRegistration.as_view(), name='registration' ),
]
