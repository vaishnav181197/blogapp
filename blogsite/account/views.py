from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView
from .forms import SignupForm,SignInForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.mail import send_mail

# Create your views here.
#create=>model,form_class,template_name->CreateView
#view a form=>form_class,template_name->FormView

# class Home(View):
#     def get(self,request):
#         return render(request,"home.html")
class Home(TemplateView):
    template_name="home.html"

# class SignUp(View):

#     def get(self,request):
#         form=SignupForm()
#         return render(request,"reg.html",{'form':form})
#     def post(self,request):
#         form_data=SignupForm(request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"User Registered Successfully")
#             return redirect('home')
#         else:
#             messages.error(request,"Registration failed")
#             return redirect('reg')

class SignUp(CreateView):
    model=User
    form_class=SignupForm
    template_name='reg.html'
    success_url=reverse_lazy('home')

    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            email_id=form_data.cleaned_data.get('email')
            uname=form_data.cleaned_data.get('username')
            pwd=form_data.cleaned_data.get('password1')
            msg="You are registered in BlogApp.\n Your username:"+str(uname)+"\n Password:"+str(pwd)
            form_data.save()
            send_mail(
                'BlogApp Registration',
                msg,
                'vaish.qis@gmail.com',
                [email_id],
                fail_silently=True
            )
            messages.success(request,"Registration Completed!!!!")
            return redirect('home')
        else:
            messages.error(request,"Registration failed")
            return render(request,"reg.html",{'form':form_data})

    

# class SignIn(View):
#     def get(self,req):
#         form=SignInForm()
#         # print(req.user)
#         return render(req,"log.html",{'form':form})
#     def post(self,req):
#         uname=req.POST.get('username')
#         psw=req.POST.get('password')
#         user=authenticate(req,username=uname,password=psw)
#         if user:
#             login(req,user)
#             return redirect('uhome')
#         else:
#             return redirect("log")

class SignIn(FormView):
    form_class=SignInForm
    template_name='log.html'
    def post(self,req):
        uname=req.POST.get('username')
        psw=req.POST.get('password')
        user=authenticate(req,username=uname,password=psw)
        if user:
            login(req,user)
            return redirect('uhome')
        else:
            messages.error(req,"Credentials are wrong")
            return redirect("log")
    

class SignOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('log')
