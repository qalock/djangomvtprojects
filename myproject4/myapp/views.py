from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myapp\home.html')


def login(request):
    return render(request,'myapp\login.html')


def register1(request):
    return render(request,'myapp\register.html')


def about1(request):
    return render(request,'myapp\about.html')


def contact(request):
    return render(request,'myapp\contact.html')