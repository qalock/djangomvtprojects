from django.urls import path 
from productapp import views

urlpatterns=[
    path('',views.product,name='productlist'),
    path('register/',views.register,name='add'),
    path('edit<int:pk>/',views.edit,name='edit'),
    path('show/<int:pk>/',views.show,name='show'),
    path('delete/<int:pk>/',views.delete,name='delete'),
]