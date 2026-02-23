from django.shortcuts import render


# Create your views here.

def home(request):
    return render('request','temapp/home.html')


def login(request):
    return render('request','temapp/login.html')


def register(request):
    return render('request','temapp/register.html')


def about(request):
    return render('request','temapp/about.html')


def contact(request):
    return render('request','temapp/contatc.html')