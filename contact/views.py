from django.shortcuts import render, redirect, get_list_or_404
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from gallery.models import Gallery


def contact_create_form(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            message = form.cleaned_data.get('message')
            messages.success(request, f'{name}, your details has been sent!, We will get to you as soon as possible. Thank You!')
            send_mail('Contact Request',f' {name} has requested to contact you. Contact Info:{phone_number}, {email}. He has left a message : {message}', 'superdjangouser@gmail.com', ['bisalgt@gmail.com'], fail_silently=True)
            return redirect('gallery_list')
    else:
        form = ContactForm()
    gallery_obj = get_list_or_404(Gallery)
    context = {'form':form, 'gallery_obj':gallery_obj}
    return render(request, 'contact/contact_us.html', context)
