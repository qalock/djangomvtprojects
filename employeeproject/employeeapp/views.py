from django.shortcuts import render

# Create your views here.

def home(request):
    dict={"name":'Ramesh Kumar',"age":25,"contact":"89564566"}
    return render(request,'employeeapp/home.html',dict)

def employee(request):
    employees=[
        {"emp_id":101,"name":"Ramesh","designation":"Developer","salary":500000},
        {"emp_id":102,"name":"Kumar","designation":"Tester","salary":600000},
        {"emp_id":103,"name":"Rahul","designation":"Manager","salary":900000},
    ]
    dict={"emp_list":employees}
    return render(request,'employeeapp/employee.html',dict)