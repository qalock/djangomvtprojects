from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home),
    path('about/',views.about),
    path('login/',views.login),
    path('contact/',views.contact),
    path('register/',views.register),
]
