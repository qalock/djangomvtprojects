from django.shortcuts import render,redirect
# from django.views.decorators.cache import never_cache

# Create your views here.
def login_view(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['pwd']
        # print(f"Username:{username}\npassword:{password}")
        if username=="admin" and password=="123":
            request.session['usname']=username
            return redirect('home')
        else:
            return render(request,'myapp/login.html',{'res':"Invalid Credentials"})

    return render(request,'myapp/login.html')


def home_view(request):
    uname=request.session.get('usname')
    if uname==None:
        return redirect('login')
    return render(request,'myapp/home.html',{'uname':uname})


def logout_view(request):
    request.session.flush()
    return render(request,'myapp/logout.html')