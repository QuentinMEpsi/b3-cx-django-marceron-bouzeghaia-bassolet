from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def signin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['mail'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'registration/signin.html')


def logout_view(request):
    logout(request)
    return render(request, 'registration/signin.html')


def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['mail'], request.POST['mail'], request.POST['password'])
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.save()
        return redirect('signin')
    else:
        return render(request, 'registration/signup.html')


def home(request):
    return render(request, 'home/home.html')


def book(request):
    return render(request, 'book/book.html')
