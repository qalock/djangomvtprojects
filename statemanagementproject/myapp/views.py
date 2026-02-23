from django.shortcuts import render

# Create your views here.
def home(request):
    print("Cookies from the client: ",request.COOKIES)
    count=int(request.COOKIES.get('count',0))
    count+=1
    response= render(request,'myapp/home.html',{'count':count})
    response.set_cookie('count',count)
    return response