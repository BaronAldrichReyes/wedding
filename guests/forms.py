from django import forms
from .models import Guest

class RSVPForm(forms.ModelForm):
    # This creates the Yes/No selection
    ATTENDANCE_CHOICES = [(True, 'Yes, I will attend!'), (False, 'No, I cannot attend.')]
    is_attending = forms.ChoiceField(choices=ATTENDANCE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'is_attending']

        