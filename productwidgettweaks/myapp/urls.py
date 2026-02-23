from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.list,name='prodlist'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('show/<int:id>/',views.show,name='show'),
    path('find/',views.find,name='find'),
    path('delete/<int:id>/',views.delete,name='delete'),
]