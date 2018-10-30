from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import RoomCreateForm
from .models import RoomDetail


class RoomCreateView(CreateView):
    form_class = RoomCreateForm
    template_name = 'rooms/room_create.html'

class RoomListView(ListView):
    model = RoomDetail
    template_name = 'rooms/room_list.html'
    context_object_name = 'room_list'
