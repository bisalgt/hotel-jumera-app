from django.shortcuts import render,redirect, get_object_or_404
from .forms import ServiceForm
from .models import Service

def service_create_form(request):
    if request.method=='POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_create.html', {'form':form})


def service_list(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request, 'services/service_list.html', context)
