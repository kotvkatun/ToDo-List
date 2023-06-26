from django.urls import path
from userauth import views

urlpatterns = [
    path("/login/", views.UserLoginView.as_view(), name="login")
]
