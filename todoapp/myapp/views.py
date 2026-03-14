from django.shortcuts import render,redirect
from .forms import DataForm
from .models import Data

# Create your views here.

def home(request):
    form=DataForm()
    if request.method=="POST":
        form=DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    data=Data.objects.all()
    return render(request,'myapp/home.html',{'form':form,'data':data})

def delete(request,id):
    data=Data.objects.get(pk=id)
    data.delete()
    return redirect('home')