from django.shortcuts import render,redirect
from django.views.generic import *
from .models import User
from .forms import RegistrationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test,login_required



# Create your views here.

class RegisterView(SuccessMessageMixin,CreateView):
    model=User
    form_class=RegistrationForm
    template_name='userapp/register.html'
    success_message="Registeration Is Successfull"


# class CustomLoginView(auth_views.LoginView):
#     template_name = 'userapp/login.html'

#     def get_success_url(self):
#         if self.request.user.is_superuser:
#             return reverse_lazy('admin_dashboard')
#         return reverse_lazy('home')

# @login_required
# def home(request):
#     return render(request,'userapp/home.html')

# @login_required
def home(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    return render(request, 'userapp/home.html')


# def admin_check(user):
#     return user.is_superuser


# @user_passes_test(admin_check)
# def admin_dashboard(request):
#     return render(request,'userapp/admin_dashboard.html')

@login_required
def login_redirect(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    return redirect('home')


class AdminDashboardView(TemplateView):
    template_name = "userapp/admin_dashboard.html"

    def test_func(self):
        return self.request.user.is_superuser
