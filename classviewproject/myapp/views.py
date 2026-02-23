from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class HelloView(View):
    def get(self,request):
        return HttpResponse("<h1>This is a class based view</h1>")