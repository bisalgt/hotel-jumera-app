from django.urls import path
from .views import RoomCreateView, RoomListView

urlpatterns = [
    path('create/', RoomCreateView.as_view(), name='room_create'),
    path('', RoomListView.as_view(), name='room_list'),
]
