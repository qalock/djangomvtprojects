from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(f'<h2>Home function in views.py {10/2}</h2>')

