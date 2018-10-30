from django import forms
from .models import Gallery, GalleryUploads


class GalleryCreateForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields ='__all__'

class GalleryUploadsCreateForm(forms.ModelForm):

    class Meta:
        model = GalleryUploads
        fields = '__all__'
