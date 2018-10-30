from django import forms
from .models import RoomDetail

class RoomCreateForm(forms.ModelForm):

    class Meta:
        model = RoomDetail
        fields = "__all__"
