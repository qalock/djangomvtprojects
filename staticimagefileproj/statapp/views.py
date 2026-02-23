from django.shortcuts import render,redirect
from .models import Statproj
from .forms import StatProjForm

# Create your views here.
def home(request):
    cardlist=Statproj.objects.all()
    return render(request,'statapp/home.html',{'cardlist':cardlist})


def add(request):
    form=StatProjForm()
    if request.method=="POST":
        form=StatProjForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    return render(request,'statapp/add.html',{'form':form})