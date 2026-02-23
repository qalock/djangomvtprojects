from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1 style='text-align:center;color:red'>This is a home component</h1>")


def login(request):
    return HttpResponse("<h1 style='text-align:center;color:pink'>This is a login component</h1>")


def about(request):
    return HttpResponse("<h1 style='text-align:center;color:blue'>This is a about component</h1>")


def contact(request):
    return HttpResponse("<h1 style='text-align:center;color:cyan'>This is a contact component</h1>")


def register(request):
    return HttpResponse("<h1 style='text-align:center;color:orange'>This is a register component</h1>")