from django.contrib import admin
from empapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=["EmployeeID","EmployeeName","EmployeeSalary","EmployeeDept"]
    class Meta:
        model=Employee
        fields='__all__'
admin.site.register(Employee,EmployeeAdmin)