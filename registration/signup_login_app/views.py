""" 
    This file contains the view functions for handling HTTP requests and generating HTTP responses.
"""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render


""" This function creates a new user account """
def SignUp(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_email = request.POST.get('email')
        user_password1 = request.POST.get('password1')
        user_password2 = request.POST.get('password2')
        if user_password1 != user_password2:
            return HttpResponse('Password and Confirm Password are not same')
        else:
            new_user = User.objects.create_user(user_name, user_email, user_password1)
            new_user.save()
            return redirect('login')
         
    return render(request, 'signup_login_app/SignUp.html')

""" This function authenticate the user and only then allows user to login into the system"""
def LogIn(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        user = authenticate(request, username = user_name, password = user_password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect ")
        
    return render(request, 'signup_login_app/LogIn.html')

"""This function only render the home page """
@login_required(login_url='login')
def Home(request):
    return render(request, 'signup_login_app/Home.html')

"""This function logout the user and redirect to login page"""
def LogOut(request):
    logout(request)
    return redirect('login')
