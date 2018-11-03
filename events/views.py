from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import FutureEventForm, PastEventForm
from .models import FutureEvent, PastEvent
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


@login_required
def future_event_create_form(request):
    if request.method=='POST':
        form = FutureEventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('future_event_list')
    else:
        form = FutureEventForm()
    return render(request, 'events/future_event_create.html', {'form':form})


def future_event_list(request):
    events = FutureEvent.objects.all()
    context = {'events': events}
    return render(request, 'events/future_event_list.html', context)

class FutureEventDeleteView(LoginRequiredMixin, DeleteView):
    model = FutureEvent
    template_name = 'events/future_event_delete.html'
    success_url = reverse_lazy('future_event_list')


@login_required
def past_event_create_form(request):
    if request.method=='POST':
        form = PastEventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('past_event_list')
    else:
        form =PastEventForm()
    return render(request, 'events/past_event_create.html', {'form':form})


def past_event_list(request):
    events = PastEvent.objects.all()
    context = {'events': events}
    return render(request, 'events/past_event_list.html', context)

class PastEventDeleteView(LoginRequiredMixin, DeleteView):
    model = PastEvent
    template_name = 'events/past_event_delete.html'
    success_url = reverse_lazy('past_event_list')
