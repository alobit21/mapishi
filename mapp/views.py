from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'home.html')
def order(request):
    return render(request, 'order.html')
def buy(request):
    return render(request, 'buy.html')
def products(request):
    return render(request, 'products.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

#loginForm
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Authentication successful, redirect to a success page
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


from .models import Image

def order(request):
    images = Image.objects.all()
    return render(request, 'order.html', {'images': images})


from django.shortcuts import render, redirect
from .forms import ImageForm

from django.shortcuts import render
from .forms import ImageUploadForm

from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_images')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_images(request):
    images = UploadedImage.objects.all()
    return render(request, 'show_images.html', {'images': images})
