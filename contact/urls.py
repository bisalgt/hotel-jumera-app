from django.urls import path
from .views import contact_create_form

urlpatterns = [
    path('', contact_create_form, name='contact_us')
]
