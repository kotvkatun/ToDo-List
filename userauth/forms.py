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
        widgets = {"password": forms.Input(attrs={"type": "password", "id": "pswd1"})}
        labels = {"username": "Username:", "password": "Password:"}


class UserRegisterForm(forms.ModelForm):
    """
    Form for registering new users
    """

    class Meta:
        model = User
        fields = ("username", "password")
        widgets = {"password": forms.Input(attrs={"type": "password", "id": "pswd1"})}
        labels = {"username": "Username:", "password": "Password:"}
    
    username = forms.CharField(required=True, max_length=20, label="Username:")
    password = forms.CharField(
        label="Password:",
        required=True,
        min_length=6,
        max_length=20,
        widget=forms.Input(attrs={"type": "password", "id": "pswd1"}),
    )
    repeat_password = forms.CharField(
        label="Repeat password:",
        required=True,
        min_length=6,
        max_length=20,
        widget=forms.Input(attrs={"type": "password", "id": "pswd2"}),
    )

    def clean(self):
        """ 
        clean() method override featuring repeat password validation
        """
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            self.add_error("confirm_password", "Password does not match")

        return cleaned_data
