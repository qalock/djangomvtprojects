from django.urls import path
from employeeapp import views


urlpatterns=[
    path('',views.home,),
    path('employee/',views.employee),
]