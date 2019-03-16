from .models import Case
from django import forms

PUBLISH_CHOICES = (
    ('personal crime', 'Personal Crimes'),
    ('property crime', 'Property Crime'),
    ('inchoate crimes', 'Inchoate Crimes'),
    ('statutory crimes', 'Statutory Crimes'),
    ('financial and other crimes', 'Financial and Other Crimes'),
    ('none', 'None')
)

class CaseForm(forms.ModelForm):
    caseType1 = forms.ChoiceField(choices=PUBLISH_CHOICES)
    caseType2 = forms.ChoiceField(choices=PUBLISH_CHOICES)
    caseType3 = forms.ChoiceField(choices=PUBLISH_CHOICES)
    class Meta:
        model = Case
        exclude = ('client', 'attorney')
        # fields = ['description']
