from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from stuapp.models import Student
from stuapp.forms import StudentForm

# Create your views here.
def student(request):
    query=request.GET.get('q')
    studentlist=Student.objects.all()
    if query:
        studentlist=Student.objects.filter(
            Q(StudentId__iexact=query) |
            Q(StudentName__icontains=query)
        )
        
    return render(request,'stuapp/student.html',{'stulist':studentlist})



def register(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form=StudentForm()
            return redirect('stulist')
        
    else:
        form=StudentForm()
    return render(request,'stuapp/register.html',{'form':form})


def edit(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('stulist')
        
    else:
        form=StudentForm(instance=student)
    return render(request,'stuapp/edit.html',{'form':form})


def show(request,pk):
    student=get_object_or_404(Student,pk=pk)
    return render(request,'stuapp/show.html',{'student':student})


def delete(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect('stulist')

