from django.shortcuts import render,redirect,get_object_or_404
from .models import Products
from .forms import ProductForm

# Create your views here.

def list(request):
    prodlist=Products.objects.all()
    return render(request,'myapp/list.html',{'prodlist':prodlist})



def edit(request,id):
    product=get_object_or_404(Products,pk=id)
    if request.method=="POST":
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('prodlist')
    else:
        form=ProductForm(instance=product)

    return render(request,'myapp/edit.html',{'form':form})



def add(request):
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prodlist')
    return render(request,'myapp/add.html',{'form':form})



def delete(request,id):
    product=get_object_or_404(Products,pk=id)
    product.delete()
    return redirect('prodlist')
    # return render(request,'myapp/delete.html')



def show(request,id):
    product=get_object_or_404(Products,pk=id)
    return render(request,'myapp/show.html',{'product':product})


def find(request):
    return render(request,'myapp/find.html')