from django.urls import path
from .views import gallery_list_view, GalleryCreateView, GalleryUploadsCreateView, GalleryUploadsListView

urlpatterns = [
    path('', gallery_list_view, name='gallery_list'),
    path('gallery_create/', GalleryCreateView.as_view(), name='gallery_create'),
    path('gallery_upload_list/', GalleryUploadsListView.as_view(), name='gallery_upload_list'),
    path('gallery_upload_create/', GalleryUploadsCreateView.as_view(), name='gallery_upload_create'),

]
