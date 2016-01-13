from django.forms import ModelForm
from django.forms.widgets import TextInput, RadioSelect

from .models import Lead


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ('__all__')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'card_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'XXXXXXXXXXXXXXXX'}),
            'expiry_date': TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': RadioSelect(attrs={'class': 'radio-select'}),
            'professional': RadioSelect(attrs={'class': 'radio-select'}),
        }
