from django.urls import path
from .views import AttorneyBidView
from .views import ClientBidView

urlpatterns = [
    path('attorney/bid/view/<int:pk>/', AttorneyBidView.as_view(),
                                        name='attorney_bid_view'),
    path('client/bid/view/<int:pk>/', ClientBidView.as_view(),
                                      name='client_bid_view'),
]
