from django.urls import path
from temapp import views


urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
]