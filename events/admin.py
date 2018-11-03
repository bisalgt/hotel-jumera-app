from django.contrib import admin
from .models import PastEvent, FutureEvent

admin.site.register(PastEvent)
admin.site.register(FutureEvent)
