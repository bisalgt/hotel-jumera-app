from django import forms
from .models import PastEvent, FutureEvent

class FutureEventForm(forms.ModelForm):
    class Meta:
        model = FutureEvent
        fields='__all__'
class PastEventForm(forms.ModelForm):
    class Meta:
        model = PastEvent
        fields='__all__'
