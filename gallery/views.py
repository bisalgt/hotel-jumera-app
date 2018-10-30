from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import GalleryCreateForm, GalleryUploadsCreateForm
from .models import Gallery, GalleryUploads


class GalleryCreateView(CreateView):
    form_class = GalleryCreateForm
    template_name = 'gallery/gallery_create.html'

class GalleryListView(ListView):
    model = Gallery
    fields = '__all__'
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'gallery_object_list'

class GalleryUploadsCreateView(CreateView):
    form_class = GalleryUploadsCreateForm
    template_name = 'gallery/gallery_upload_create.html'

class GalleryUploadsListView(ListView):
    model = GalleryUploads
    fields = '__all__'
    template_name = 'gallery/gallery_upload_list.html'
    context_object_name = 'gallery_upload_object_list'
