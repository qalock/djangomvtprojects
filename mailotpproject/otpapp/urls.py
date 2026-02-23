from django.urls import path
from otpapp import views

urlpatterns=[
    path('',views.send_otp,name='send_otp'),
    path('verify/',views.verify_otp,name='verify'),

]