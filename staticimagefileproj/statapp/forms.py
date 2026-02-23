from django import forms
from .models import Statproj


class StatProjForm(forms.ModelForm):


    class Meta:
        model=Statproj
        fields=['title','image']