from .models import Case
from django import forms
from utils import ATTRONEY_SPECIALITIES

PUBLISH_CHOICES = tuple((speciality.lower(), speciality.title()) for speciality in
                    ATTRONEY_SPECIALITIES) + tuple((('other', 'Other'),))

class CaseForm(forms.ModelForm):
    caseType1 = forms.ChoiceField(choices=PUBLISH_CHOICES)
    caseType2 = forms.ChoiceField(choices=PUBLISH_CHOICES)
    caseType3 = forms.ChoiceField(choices=PUBLISH_CHOICES)
    class Meta:
        model = Case
        exclude = ('client', 'attorney')
        # fields = ['description']
