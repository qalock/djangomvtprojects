from django import forms
from .models import User

# Create your models here.

class SignUpForm(forms.ModelForm):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)

    class Meta:
        model=User
        fields=['email','username','password']

        widgets={
            'password':forms.PasswordInput()
        }