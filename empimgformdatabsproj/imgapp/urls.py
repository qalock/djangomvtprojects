from django.urls import path
from imgapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.employee,name='emplist'),
    path('register/',views.register,name='add'),
]

# Source - https://stackoverflow.com/q
# Posted by Floris Kruger, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-08, License - CC BY-SA 4.0

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
