from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.shortcuts import reverse, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from .forms import UserLoginForm, UserRegisterForm
from .models import User
from todo.models import ToDoLists


# Create your views here.
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(
            request,
            "login.html",
            {"message": "Invalid username and/or password."},
        )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            todolist = ToDoLists.objects.create(owner=user)
            todolist.save()
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            return render(
                request,
                "register.html",
                {"message": "Username already taken."},
            )
    return render(request, "register.html")
