from .models import Attorney
from .models import Client
from .models import Users
from django import forms
from utils import ATTRONEY_SPECIALITIES

YEARS= [x for x in range(1940,2021)]

PUBLISH_CHOICES = tuple((speciality.lower(), speciality.title()) for speciality in
                    ATTRONEY_SPECIALITIES) + tuple((('none', 'None'),))

class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        # exclude = ('birthDate',)
        fields = ('firstName', 'lastName', 'birthDate','email', 'username', 'password')


class AttorneyRegistrationForm(ClientRegistrationForm):
    speciality = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=PUBLISH_CHOICES,
    )
    class Meta(ClientRegistrationForm.Meta):
        fields = ClientRegistrationForm.Meta.fields + ('speciality',)
