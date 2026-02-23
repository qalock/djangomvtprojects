from django.urls import path,include
from myapp.views import *


urlpatterns=[
    path('',home),
    path('java/',java_exam_view),
    path('python/',python_exam_view),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',register),
    path('logout/',logout_view),
]