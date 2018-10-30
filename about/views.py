from django.shortcuts import render, redirect, get_object_or_404
from .forms import AboutForm
from .models import About


def about_create_form(request):
    about = get_object_or_404(About)
    if request.method=='POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about_detail')
    else:
        form = AboutForm( instance=about)
    return render(request, 'about/about_create.html', {'form':form})


def about_detail(request):
    about_company = About.objects.all()
    context = {'about': about_company}
    return render(request, 'about/about_detail.html', context)
