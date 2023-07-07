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
        widgets = {
            "username": forms.widgets.Input(attrs={"type": "text", "maxlength": 20}),
            "password": forms.widgets.Input(
                attrs={"type": "password", "id": "pswd1", "maxlength": 20}
            ),
        }
        labels = {"username": "Username:", "password": "Password:"}


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "password", "email")
        widgets = {
            "username": forms.widgets.Input(attrs={"type": "text", "maxlength": 20}),
            "password": forms.widgets.Input(
                attrs={
                    "type": "password",
                    "id": "id_password",
                    "onkeyup": "check()",
                    "maxlength": 20,
                }
            ),
        }
        labels = {"username": "Username:", "password": "Password:"}
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    