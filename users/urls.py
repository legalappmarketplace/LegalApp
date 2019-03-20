from django.contrib import admin
from django.urls import path
from .views import ClientRegistration
from .views import UserLogin
from .views import UserLogout
from .views import AttorneyRegistration
urlpatterns = [
    path('client/register/', ClientRegistration.as_view(), name='client_registration' ),
    path('attorney/register/', AttorneyRegistration.as_view(), name='client_registration' ),
    path('login/', UserLogin.as_view(), name='user_login' ),
    path('login/?next=<str:next_page>', UserLogin.as_view(), name='user_login' ),
    path('logout/', UserLogout.as_view(), name='user_logout' ),
]
