from django.urls import path
from userapp.views import *
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',home,name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='userapp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='home'),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path("admin-dashboard/", AdminDashboardView.as_view(), name="admin_dashboard"),
    path('login-redirect/', login_redirect, name='login_redirect'),
    # path('login//',CustomLoginView.as_view(),name='loginn'),
    # path('admin-dashboard/',admin_dashboard,name='admin_dashboard'),
    # path('login-redirect/',login_redirect,name='login_redirect'),
]