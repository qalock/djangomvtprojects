from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',Products.as_view(),name='list'),
    path('create/',AddProduct.as_view()),
    path('edit/<int:pk>/',EditProduct.as_view()),
    path('delete/<int:pk>/',DeleteProduct.as_view()),
    path('<int:pk>/',ShowProduct.as_view()),
]