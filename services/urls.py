from django.urls import path
from .views import service_create_form, service_list

urlpatterns=[
    path('', service_list, name='service_list'),
    path('create/', service_create_form, name='service_create'),
]
