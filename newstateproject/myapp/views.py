from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    uname=request.COOKIES.get("usrename")
    pwd=request.COOKIES.get("passord")
    return render(request,'myapp/home.html',{'username':uname,'password':pwd})

def login(request):
    if request.method=="POST":
        uame=request.POST['uname']
        pwod=request.POST['pwd']
        response=redirect('/home/')
        response.set_cookie('usrename',uame,max_age=3600)
        response.set_cookie('passord',pwod,max_age=3600)
        return response
    return render(request,'myapp/login.html')

def register(request):
    uname=request.COOKIES.get("usrename")
    pwd=request.COOKIES.get("passord")
    return render(request,'myapp/register.html',{'username':uname,'password':pwd})