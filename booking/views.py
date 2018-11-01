from django.views.generic import CreateView
from .forms import BookingForm
from .models import Booking
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib import messages


def register(request):
    if request.method=='POST':
        form = BookingForm(request.POST)
        if form .is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            room = form.cleaned_data.get('room')
            check_in = form.cleaned_data.get('check_in')
            check_out = form.cleaned_data.get('check_out')
            adult = form.cleaned_data.get('adult')
            child = form.cleaned_data.get('child')
            messages.success(request,f' {name}, Your Booking has been successful for {room}, from {check_in} to {check_out} with {adult} adults and {child} childrens.Thank You!!!')
            send_mail(f'Booking BY {name} ',  f'A booking has been made for {room} , from {check_in} to {check_out} with {adult} adults and {child} childrens.', 'superdjangouser@gmail.com',['bisalgt@gmail.com'], fail_silently=True)
            return redirect('gallery_list')
    else:
        form = BookingForm()
    return render(request,'booking/booking_create.html',{"form":form})
