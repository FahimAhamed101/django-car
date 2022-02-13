from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

from contacts.models import Contacts
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
       
        if user is  not None:
            auth.login(request,user)
            messages.success(request,'you are logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid login credential')
            return redirect('login')
    return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['flastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_passord=request.POST['confirm_passord']
        if password==confirm_passord:
            if User.objects.filter(username=username).exists():
                messages.error(request,'name already exist')
                return render('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exist!')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                    auth.login(request,user)
                    messages.success(request,'you are now logged in succesfully')
                    return redirect('dasboard')
                    user.save()
                    messages.success(request,'you are registered succesfully')
                    return redirect('login')


    return render(request, 'accounts/register.html')

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.success(request,'you are succesfully logged out')
        return redirect('home')
        
    return redirect('home')


@login_required(login_url= 'login')
def dashboard(request):
  
    user_inquiry=Contacts.objects.order_by('-created_date').filter(user_id=request.user.id)

    data={
        'inquiries':user_inquiry,
    }


    return render(request, 'accounts/dashboard.html',data)


