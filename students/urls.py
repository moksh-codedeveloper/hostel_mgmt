from .views import dashboard, register, student_profile, user_login, register_user, user_logout, update_student, update_user
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("student/create/", register_user, name="student_create"),
    path("student/", student_profile, name="student_profile"),
    path("logout/", user_logout, name="user_logout"),
    path("student/update/", update_student, name="student_update"),
    path("user/update/", update_user, name="user_update"),
    path("dashboard/", dashboard, name="dashboard")
]
