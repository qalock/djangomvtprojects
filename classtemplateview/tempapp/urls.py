from django.urls import path
from tempapp.views import *

urlpatterns=[
    path('',Home.as_view(),name='list'),
    path('register/',Register.as_view(),name='add'),
    path('edit/<int:pk>/',Edit.as_view(),name='edit'),
    path('show/<int:pk>/',Show.as_view(),name='show'),
    path('delete/<int:pk>/',Delete.as_view(),name='delete'),
]