from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView, CreateView
from .forms import UserLoginForm, UserRegisterForm
from .models import User


# Create your views here.
class UserLoginView(FormView):
    """ 
    View for user login
    """
    template_name = "login.html"
    form_class = UserLoginForm

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=username, password=password)      
        if user is not None:
            login(self.request, user)
            return None
        else:
            pass

class UserRegisterView(FormView):
    template_name = "register.html"
    form_class = UserRegisterForm
    fields = ['username', 'password']