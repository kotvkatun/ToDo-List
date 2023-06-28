"""
Form classes for userauth app. 
Contains UserLogin and UserRegister ModelForms.
"""
from django import forms
from .models import User

# Create forms here


class UserLoginForm(forms.ModelForm):
    """
    Form for user login with corresponding fields
    """

    class Meta:
        model = User
        fields = ("username", "password")
        widgets = {"password": forms.widgets.Input(attrs={"type": "password", "id": "pswd1"})}
        labels = {"username": "Username:", "password": "Password:"}


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "password")
        widgets = {"password": forms.widgets.Input(attrs={"type": "password", "id": "id_password", "onkeyup": "check()"})}
        labels = {"username": "Username:", "password": "Password:"}


