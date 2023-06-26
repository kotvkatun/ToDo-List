from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserLoginForm


# Create your views here.
class UserLoginView(FormView):
    """ 
    View for user login
    """
    template_name = "login.html"
    form_class = UserLoginForm

    def form_valid(self, form):
        pass
