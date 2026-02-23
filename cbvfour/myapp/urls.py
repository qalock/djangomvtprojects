from django.urls import path
from myapp.views import *


urlpatterns=[
    path('',Students.as_view(),name='list'),
    path('create/',AddStudent.as_view()),
    path('<int:pk>/',DetailStudent.as_view()),
    path('edit/<int:pk>/',EditStudent.as_view()),
    path('delete/<int:pk>/',DeleteStudent.as_view()),
]