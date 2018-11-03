from django.urls import path
from .views import future_event_create_form, future_event_list,past_event_create_form,past_event_list, FutureEventDeleteView, PastEventDeleteView

urlpatterns= [
    path('future_event_list/', future_event_list, name='future_event_list'),
    path('future_event_create/', future_event_create_form, name='future_event_create'),
    path('past_event_list/', past_event_list, name='past_event_list'),
    path('past_event_create/', past_event_create_form, name='past_event_create'),
    path('<int:pk>/future_event_delete', FutureEventDeleteView.as_view(), name='future_event_delete'),
    path('<int:pk>/past_event_delete/', PastEventDeleteView.as_view(), name='past_event_delete'),
]
