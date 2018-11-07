from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import GalleryCreateForm, GalleryUploadsCreateForm
from .models import Gallery, GalleryUploads
from contact.forms import ContactForm
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from booking.forms import BookingForm





class GalleryCreateView(LoginRequiredMixin, CreateView):
    form_class = GalleryCreateForm
    template_name = 'gallery/gallery_create.html'


def gallery_list_view(request):
    gallery_object_list = Gallery.objects.all()

    if request.method=='POST':
        contact_form = ContactForm(request.POST)
        booking_form = BookingForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            name = contact_form.cleaned_data.get('name')
            email = contact_form.cleaned_data.get('email')
            phone_number = contact_form.cleaned_data.get('phone_number')
            message = contact_form.cleaned_data.get('message')
            messages.success(request, f'{name}, your details has been sent!, We will get to you as soon as possible. Thank You!')
            send_mail('Contact Request',f' {name} has requested to contact you. Contact Info:{phone_number}, {email}. He has left a message : {message}', 'superdjangouser@gmail.com', ['bisalgt@gmail.com'], fail_silently=True)
            return redirect('gallery_list')


        if booking_form .is_valid():
            booking_form.save()
            name = booking_form.cleaned_data.get('name')
            room = booking_form.cleaned_data.get('room')
            check_in = booking_form.cleaned_data.get('check_in')
            check_out = booking_form.cleaned_data.get('check_out')
            adult = booking_form.cleaned_data.get('adult')
            child = booking_form.cleaned_data.get('child')
            messages.success(request,f' {name}, Your Booking has been successful for {room}, from {check_in} to {check_out} with {adult} adults and {child} childrens.Thank You!!!')
            send_mail(f'Booking BY {name} ',  f'A booking has been made for {room} , from {check_in} to {check_out} with {adult} adults and {child} childrens.', 'superdjangouser@gmail.com',['bisalgt@gmail.com'], fail_silently=True)
            return redirect('gallery_list')
    else:
        contact_form = ContactForm()
        booking_form = BookingForm()
    context = {'booking_form':booking_form, 'contact_form':contact_form, 'gallery_object_list':gallery_object_list}
    return render(request, 'gallery/gallery_list.html', context)


class GalleryUploadsCreateView(LoginRequiredMixin, CreateView):
    form_class = GalleryUploadsCreateForm
    template_name = 'gallery/gallery_upload_create.html'

class GalleryUploadsListView(ListView):
    model = GalleryUploads
    fields = '__all__'
    template_name = 'gallery/gallery_upload_list.html'
    context_object_name = 'gallery_upload_object_list'
    paginate_by = 9
