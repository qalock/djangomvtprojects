from django.urls import path
from myapp.views import *
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',home,name="home"),
    path('register/',register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
]