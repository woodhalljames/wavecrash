from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
class SigninView(generic.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'app_user/signin.html')

    def post(self, *args, **kwargs):
        username = self.request.POST.get('singin-email')
        password = self.request.POST.get('signin-pass')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(self.request, user)

                return HttpResponseRedirect(reverse('app_user:account'))
            else:
                messages.error(self.request, 'Your account has been deactivated')
                return HttpResponseRedirect(reverse('app_user:signin'))
        else:
            messages.error(self.request, 'Please use correct email and password combination')
            return HttpResponseRedirect(reverse('app_user:signin'))

class SignupView(generic.View):
    def get(self, *args, **kwargs):
        context = {
            'user_creation_form': CreateUserForm(),
            'appuserform': AppUserForm()
        }
        return render(self.request, 'app_user/signup.html', context)

    def post(self, *args, **kwargs):
        userForm = CreateUserForm(data=self.request.POST)
        appUserForm = AppUserForm(data=self.request.POST)
        
        if userForm.is_valid() and appUserForm.is_valid():
            user = userForm.save(commit=False)
            # checking if the email already exists
            email_check = User.objects.filter(email=user.email)
            if email_check.count():
                messages.error(self.request, 'This email already exists. signin using the same email or choose another email.')
                return render(self.request, 'app_user/signup.html', {'user_creation_form': userForm,
                                                                 'appuserform':AppUserForm})
            else:
                user.username = user.email
                name = user.first_name
                user.first_name = name.split(' ')[0]
                user.last_name = name.split(' ')[-1]
                user.save()

                appuser = appUserForm.save(commit=False)
                appuser.user = user
                appuser.save()

                messages.success(self.request, 'Your profile was created. Login to enter into store.')
                
                return HttpResponseRedirect(reverse('app_user:signin'))
        else:
            messages.error(self.request, 'Something went wrong. Try again')
            return render(self.request, 'app_user/signup.html', {'user_creation_form': userForm,
                                                                 'appuserform':AppUserForm})
@login_required()
def signoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

class AccountView(LoginRequiredMixin,generic.View):
    login_url = '/user/signin'
    redirect_field_name = '/user/account/'
    
    def get(self, *args, **kwargs):
        context = {
       # 'orders':Order.objects.filter(user=self.request.user, ordered=True).order_by('-id')
        }
        return render(self.request, 'app_user/account.html', context)        