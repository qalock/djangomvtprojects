from django.urls import path
from myapp.views import HelloView
#from myapp import views

urlpatterns=[
    path('',HelloView.as_view()),
]