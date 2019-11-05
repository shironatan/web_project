from django.shortcuts import redirect,render
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.views import View

from .forms import LoginForm

# Create your views here.
#Login function
class Account_login(View):
    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            # ログイン済みだった場合　トップ画面にリダイレクト
            return redirect('/')
        else:
            form = LoginForm(request.POST)
            return render(request,'registration/login.html',{'form':form,})

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request,user)
            return redirect('home')
        return render(request,'registration/login.html',{'form':form,})


#Logout function
class Account_logout(View):
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            # ログイン済みだった場合
            return self.post(*args,**kwargs)
            print('wa')
        else:
            return redirect('/')

    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(request)
        return redirect('home')