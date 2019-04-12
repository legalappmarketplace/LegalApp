from django.contrib import admin
from django.urls import path
from .views import CaseCreateView
from .views import CaseDetailView
from .views import CaseListView
from .views import UsersCases
urlpatterns = [
    path('case/<int:pk>', CaseDetailView.as_view(), name='case_detail_view'),
    path('list/', CaseListView.as_view(), name='case_list_view' ),
    path('upload/', CaseCreateView.as_view(), name='case_create_view'),
    path('user/cases/', UsersCases.as_view(), name='users_cases'),
]
