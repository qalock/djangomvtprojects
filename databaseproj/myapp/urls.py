from django.urls import path
from myapp import views


urlpatterns=[
    path('',views.employees,name='emplist'),
    path('register/',views.register,name='add'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('show/<int:id>/',views.show,name='show'),
    path('delete/<int:id>/',views.delete,name='delete'),
]