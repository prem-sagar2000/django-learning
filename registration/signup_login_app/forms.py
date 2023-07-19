"""This file contains Signup and Login Forms created using Django Forms"""
from django import forms


class SignUpForm(forms.Form):
    """This class creates a SignUp form using Django Forms"""
    username = forms.CharField(
        label="Enter Username",
        max_length=100,
        required= True,
        widget= forms.TextInput(attrs={'placeholder': 'Enter username'})
    )
    email = forms.EmailField(
        label="Enter Email",
        max_length=200,
        required= True,
        widget= forms.TextInput(
            attrs={'placeholder': 'Enter your email'}
        )
    )
    company = forms.CharField(
        label="Enter Company Name",
        max_length=200,
        required= True,
        widget= forms.TextInput(attrs={'placeholder': 'Enter Company Name'})
    )
    password1 = forms.CharField(
        required=True,
        label="Enter Password",
        widget= forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}
        )
    )
    password2 = forms.CharField(
        required=True,
        label="Confirm Password",
        widget= forms.PasswordInput(
            attrs={'placeholder': 'Confirm your password'}
        )
    )
    
class LogInForm(forms.Form):
    """This class creates a LogIn form using Django Forms"""
    username = forms.CharField(
        label="Enter Username",
        max_length=100,
        required= True,
        widget= forms.TextInput(
            attrs={'placeholder': 'Enter username'}
        )
    ) 
    password = forms.CharField(
        required=True,
        label="Enter Password",
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter Password'}
        )
    )
    