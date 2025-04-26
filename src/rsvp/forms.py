from django import forms

from .models import RSVP


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = [
            'name',
            'email',
            'companion',
            'companion_email',
            'message',
            'confirmed',
        ]
        labels = {
            'companion': 'Nome do Acompanhante (opcional)',
            'companion_email': 'E-mail do Acompanhante (opcional)',
            'message': 'Mensagem (opcional)',
            'confirmed': 'Estou ciente do meu compromisso',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['confirmed'].required = True
