from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login

from .models import KawasanBerikat, UploadDocument
from .forms import KawasanBerikatForm, UploadDocumentForms
from upload import models

# Create your views here.


def index(request):
    return render(request, 'index.html')


def profil(request):
    return render(request, 'upload/profil.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


class kawasanberikat_view(CreateView):
    form_class = KawasanBerikatForm
    template_name = 'upload/kawasanberikat.html'
    success_url = reverse_lazy('kawasanberikat')


class kawasanberikat_all_view(ListView):
    model = KawasanBerikat
    template_name = 'upload/list/kawasanberikat_list.html'


class kawasanberikat_delete_view(DeleteView):
    model = KawasanBerikat
    success_url = reverse_lazy('kawasanberikat_all_view')


class upload_view(CreateView):
    form_class = UploadDocumentForms
    template_name = 'upload/upload.html'
    success_url = reverse_lazy('kawasanberikat')


class upload_all_view(ListView):
    model = UploadDocument
    template_name = 'upload/list/upload_list.html'


class upload_delete_view(DeleteView):
    model = UploadDocument
    success_url = reverse_lazy('upload_all_view')
