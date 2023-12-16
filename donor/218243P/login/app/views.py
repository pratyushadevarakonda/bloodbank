from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authentication(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('app:homepage')
        else:
            messages.info(request,'Invalid user credentials')
            return redirect('app:login')
    else:
        return render(request,'login.html')
def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pass1']
        password2=request.POST['pass2']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already taken")
            return redirect('app:registration')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('app:login')
    return render(request,'registration.html')
def homepage(request):
    return HttpResponse('HomePage')