from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1 style='text-align:center'>Welcome home function</h1>")


def login(request):
    return HttpResponse("<h1 style='text-align:center' color:red>Welcome Login function</h1>")

def register(request):
    return HttpResponse("<h1 style='text-align:center' color:yellow >Welcome Register function</h1>")

def about(request):
    return HttpResponse("<h1 style='text-align:center' color:'pink'>Welcome About function</h1>")


def contact(request):
    return HttpResponse("<h1 style='text-align:center color:'red''>Welcome contact function</h1>")