from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Otp
import random
from django.http import HttpResponse


# Create your views here.

def generate_otp():
    return str(random.randint(100000,999999))


def send_otp(request):
    if request.method == "POST":
        email = request.POST.get('email')

        otp = generate_otp()

        Otp.objects.create(email=email, otp=otp)

        # Instead of sending mail, send OTP to frontend
        return render(request, "otpapp/verify.html", {
            "email": email,
            "otp": otp   # send otp to template
        })

    return render(request, "otpapp/send.html")



def verify_otp(request):
    if request.method == "POST":
        email = request.POST['email']
        user_otp = request.POST['otp']

        try:
            record = Otp.objects.filter(email=email).last()

            if record.otp == user_otp:
                return HttpResponse("OTP Verified ✅")
            else:
                return HttpResponse("Invalid OTP ❌")

        except:
            return HttpResponse("OTP Not Found")

    return render(request, 'otpapp/verify.html')