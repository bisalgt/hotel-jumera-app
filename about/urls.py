from django.urls import path
from .views import about_create_form, about_detail

urlpatterns=[
    path('', about_detail, name='about_detail'),
    path('create/', about_create_form, name='about_create'),
]
