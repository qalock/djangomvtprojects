from django.contrib import admin
from .models import Statproj

# Register your models here.

class StatprojAdmin(admin.ModelAdmin):
    list_display=['title','image']

    class Meta:
        model=Statproj
        fields='__all__'

admin.site.register(Statproj,StatprojAdmin)