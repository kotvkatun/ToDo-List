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
    """
    Form for registering new users
    """

    class Meta:
        model = User
        fields = ("username", "password")
        widgets = {"password": forms.widgets.Input(attrs={"type": "password", "id": "pswd1"})}
        labels = {"username": "Username:", "password": "Password:"}
        errors = {
            "username": {
                "min_length": "Username can not be shorter than 5 characters",
                "max_length": "Username can not be longer than 20 characters",
                "unique": "The name you chose has already been taken. Please choose a different name.",
            },
            "password": {
                "min_length": "Password can not be shorter than 6 characters.",
                "max_length": "Password can not be longer that 20 characters.",
            },
        }

    repeat_password = forms.CharField(
        label="Repeat password:",
        required=True,
        min_length=6,
        max_length=20,
        widget=forms.widgets.Input(attrs={"type": "password", "id": "pswd2"}),
    )

    def clean(self):
        """
        clean() method override featuring repeat password validation
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            self.add_error("confirm_password", "Password does not match")

        return cleaned_data
