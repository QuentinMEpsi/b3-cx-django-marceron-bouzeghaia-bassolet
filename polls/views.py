from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'connect/login.html')


def register(request):
    return render(request, 'connect/register.html')


def home(request):
    return render(request, 'home/home.html')
