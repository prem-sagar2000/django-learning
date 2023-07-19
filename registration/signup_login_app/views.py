""" 
    This file contains the view functions for handling HTTP requests and generating HTTP responses.
"""
from .forms import SignUpForm, LogInForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, render


def SignUp(request):
    # """ This function creates a new user account """
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_email = request.POST.get('email')
        company = request.POST.get('company')
        user_password1 = request.POST.get('password1')
        user_password2 = request.POST.get('password2')
        if user_password1 != user_password2:
            return HttpResponse('Password and Confirm Password are not same')
        else:
            new_user = CustomUser.objects.create_user(username = user_name, email = user_email, password = user_password1, company = company)
            new_user.save()
            return redirect('login')
        
    form = SignUpForm() 
    return render(request, 'signup_login_app/signup.html', {'form' : form}) 

def LogIn(request):
    """ This function authenticate the user and only then allows user to login into the system"""
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        user = authenticate(request, username = user_name, password = user_password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect ")
        
    form = LogInForm()
    return render(request, 'signup_login_app/login.html', {'form' : form}) 

@login_required(login_url='login')
def Home(request):
    """This function only render the home page """
    user = request.user
    username = user.username
    email = user.email  
    company = user.company  
    return render(request, 'signup_login_app/home.html', {'username': username , 'email': email, 'company': company})

def LogOut(request):
    """This function logout the user and redirect to login page"""
    logout(request)
    return redirect('login')
