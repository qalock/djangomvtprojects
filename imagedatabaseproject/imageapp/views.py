from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import ProductForm
from django.db.models import Q


# Create your views here.
def product(request):
    query=request.GET.get('q')
    p=Product.objects.all()
    if query:
        p=Product.objects.filter(
            Q(id__iexact=query) |
            Q(productname__icontains=query)
        )
    return render(request,'imageapp/product.html',{'prodlist':p})


def register(request):
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prodlist')

    return render(request,'imageapp/register.html',{'form':form})


def edit(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=="POST":
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('prodlist')
    else:
        form=ProductForm(instance=product)
    return render(request,'imageapp/edit.html',{'form':form})


def show(request,pk):
    product=get_object_or_404(Product,pk=pk)
    return render(request,'imageapp/show.html',{'product':product})


def delete(request,pk):
    product=get_object_or_404(Product,pk=pk)
    product.delete()
    return redirect('prodlist')