from django.urls import path
from .views import register, student_profile, user_login, register_user, user_logout, update_student

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("student/create/", register_user, name="user_register"),
    path("student/", student_profile, name="student_profile"),
    path("logout/", user_logout, name="user_logout"),
    path('update/', update_student, name="update_student")
]
