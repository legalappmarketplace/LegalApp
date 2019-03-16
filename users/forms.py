from .models import Attorney
from .models import Client
from .models import Users
from django import forms

PUBLISH_CHOICES = (
    ('attorney', 'Attorney'),
    ('client', 'None Attorney')
)
YEARS= [x for x in range(1940,2021)]

class RegisterForm(forms.ModelForm):
    userType = forms.ChoiceField(choices=PUBLISH_CHOICES)
    # birthDate = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    # firstName = forms.CharField(max_length=500)
    # lastName = forms.CharField(max_length=500)
    # birthDate = forms.DateField()
    # email = forms.EmailField()
    # username = forms.CharField(max_length=500)
    # password = forms.CharField(max_length=500)
    class Meta:
        model = Users
        # exclude = ('birthDate',)
        fields = ['firstName', 'lastName', 'birthDate','email', 'username', 'password']
