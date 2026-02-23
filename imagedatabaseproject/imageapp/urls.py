from django.urls import path
from imageapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.product,name='prodlist'),
    path('register/',views.register,name='add'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('show/<int:pk>/',views.show,name='show'),
    path('delete/<int:pk>/',views.delete,name='delete'),
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)