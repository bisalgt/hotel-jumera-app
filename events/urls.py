from django.urls import path
from .views import event_create_form, event_list

urlpatterns= [
    path('', event_list, name='event_list'),
    path('create/', event_create_form, name='event_create'),
]
