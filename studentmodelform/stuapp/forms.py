from django import forms
from stuapp.models import Student


class StudentForm(forms.ModelForm):
    StudentId=forms.IntegerField()
    StudentName=forms.CharField(max_length=60)
    StudentAge=forms.IntegerField()
    StudentEmail=forms.EmailField()


    class Meta:
        model=Student
        fields='__all__'