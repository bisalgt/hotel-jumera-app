from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event


def event_create_form(request):
    if request.method=='POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_create.html', {'form':form})


def event_list(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'events/event_list.html', context)
