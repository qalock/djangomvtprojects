from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register1/',views.register1,name='register1'),
    path('about1/',views.about1,name='about1'),
    path('contact/',views.contact,name='contact'),
]