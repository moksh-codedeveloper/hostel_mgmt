from django.urls import path
from .views import register, student_profile, user_login, register_user, user_logout

urlpatterns = [
    path("register/", register),
    path("login/", user_login),
    path("student/create/", register_user),
    path("student/", student_profile),
    path("logout/", user_logout)
]
