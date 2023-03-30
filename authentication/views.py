from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,get_user_model,logout
from django.views import View
from .forms import CreationForm
# Create your views here.


class SignupView(View):
    def get(self, request, *args, **kwargs):
        form = CreationForm()
        return render(request,'signup.html',{'form':form})

    def post(self, request ,*args, **kwargs):
        form = CreationForm(request.POST)
        if form.is_valid():
            print("Yes")
            print(request.POST['username'])
            form.save()
            return redirect('/auth/login')
        else:
            return render(request,'signup.html',{'form':form})

class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request , *args , **kwargs):
        form = self.form_class()
        return render(request, self.template_name , {'form': form})
    
    def post(self, request , *args , **kwargs):
        form = self.form_class(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')
        return render(request, self.template_name , {'form': form})

class LogoutView(View):

    def get(self, request , *args , **kwargs):
        logout(request)
        return redirect('/auth/login/')