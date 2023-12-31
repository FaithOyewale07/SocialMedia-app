from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username'],
        email = request.POST['email'],
        password = request.POST['password'],
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request, 'Password don\'t Match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')


def profile(request):
    return render(request, 'profile.html')


def setting(request):
    return render(request, 'setting.html')
