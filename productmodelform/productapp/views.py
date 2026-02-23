from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from productapp.models import Product
from productapp.forms import ProductForm

# Create your views here.
def product(request):
    query=request.GET.get('q')
    productlist=Product.objects.all()
    if query:
        productlist=Product.objects.filter(
            Q(ProductId__iexact=query) |
            Q(ProductName__icontains=query)
        )
    
    return render(request,'productapp/product.html',{'productlist':productlist})


def register(request):
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('productlist')
    return render(request,'productapp/register.html',{'form':form})


def edit(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=="POST":
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('productlist')
    else:
        form=ProductForm(instance=product)
    return render(request,'productapp/edit.html',{'form':form})


def show(request,pk):
    product=get_object_or_404(Product,pk=pk)
    return render(request,'productapp/show.html',{'product':product})


def delete(request,pk):
    product=get_object_or_404(Product,pk=pk)
    product.delete()
    return redirect('productlist')