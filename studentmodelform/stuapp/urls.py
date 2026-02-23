from django.urls import path
from stuapp import views

urlpatterns=[
    path('',views.student,name='stulist'),
    path('register/',views.register,name='add'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('show/<int:pk>/',views.show,name='show'),
    path('delete/<int:pk>/',views.delete,name='delete'),
]