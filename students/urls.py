from django.urls import path
from .views import register, user_login, register_user

urlpatterns = [
    path("register/", register),
    path("login/", user_login),
    path("student/create/", register_user),
]
