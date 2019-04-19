from django.urls import path
from .views import AttorneyBidView

urlpatterns = [
    path('attorney/bid/view/<int:pk>/', AttorneyBidView.as_view(), name='case_detail_view'),
]
