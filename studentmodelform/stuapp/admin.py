from django.contrib import admin
from stuapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=["StudentId","StudentName","StudentAge","StudentEmail"]

admin.site.register(Student,StudentAdmin)