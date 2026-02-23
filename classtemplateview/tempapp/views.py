from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Student
from .forms import StudentForm

# Create your views here.

class Home(TemplateView):
    template_name='tempapp/home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['students']=Student.objects.all()
        return context


class Register(TemplateView):
    template_name='tempapp/register.html'

    def get(self, request, *args, **kwargs):
        form=StudentForm()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request, *args, **kwargs):
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request,self.template_name,{'form':form})



class Show(TemplateView):
    template_name = 'tempapp/show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = Student.objects.get(pk=self.kwargs['pk'])
        return context
    


class Edit(TemplateView):
    template_name = 'tempapp/edit.html'

    def get(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs['pk'])
        form = StudentForm(instance=student)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs['pk'])
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, self.template_name, {'form': form})
    

class Delete(TemplateView):
    template_name = 'tempapp/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = Student.objects.get(pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        Student.objects.get(pk=kwargs['pk']).delete()
        return redirect('list')