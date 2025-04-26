from django import forms

from .models import RSVP


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['name', 'companion', 'message', 'confirmed']
        labels = {
            'companion': 'Nome do Acompanhante (opcional)',
            'confirmed': 'Me comprometo em estar presente na cerimônia',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['confirmed'].required = True
