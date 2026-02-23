from django.urls import path,include
from myapp.views import *


urlpatterns=[
    path('',home),
    path('register/',register),
    path('emplist/',employee,name='emplist'),
    path('add/',addemp),
    path('logout/',logout_view),
    path('delete/<int:pk>/',delete),
    path('<int:pk>/',view),
    path('edit/<int:pk>/',edit),
    path('accounts/',include('django.contrib.auth.urls')),
]