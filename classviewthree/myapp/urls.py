from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',Employees.as_view(),name='list'),
    path('create/',AddEmployee.as_view(),name='create'),
    path('edit/<int:pk>/',EditEmployee.as_view(),name='edit'),
    path('<int:pk>/',FindEmployee.as_view(),name='show'),
    path('delete/<int:pk>/',DeleteEmployee.as_view(),name='delete'),
]