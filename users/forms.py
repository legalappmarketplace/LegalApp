from .models import Attorney
from .models import Client
from .models import CustomUser
from django import forms
from utils import ATTRONEY_SPECIALITIES

YEARS= [x for x in range(1940,2021)]

PUBLISH_CHOICES = tuple((speciality.lower(), speciality.title()) for speciality in
                    ATTRONEY_SPECIALITIES) + tuple((('none', 'None'),))

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # exclude = ('birthDate',)
        fields = ('firstName', 'lastName', 'birthDate','email', 'username','password')

class CustomUserChangeForm(UserRegistrationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username')

class AttorneyRegistrationForm(UserRegistrationForm):
    speciality = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=PUBLISH_CHOICES,
    )
    # about = forms.Textarea()
    class Meta(UserRegistrationForm.Meta):
        fields = UserRegistrationForm.Meta.fields + ( 'about', 'speciality',)
