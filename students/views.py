from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import User, Student
from .forms import StudentUpdateForm, UserUpdateForm
from django.shortcuts import redirect, render, get_object_or_404

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        full_name = request.POST.get("full_name")

        if User.objects.filter(username=username).exists():
            return render(request, "registration/registration.html", {
                "error": "Username already exists"
            })

        user = User.objects.create_user(
            username=username,
            password=password,
            full_name=full_name
        )

        login(request, user)

        return redirect("student_create")

    return render(request, "registration/registration.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if not user:
            return render(request, "registration/login.html", {
                "error": "Invalid credentials"
            })

        login(request, user)

        if not hasattr(user, "student"):
            return redirect("student_create")

        return redirect("dashboard")

    return render(request, "registration/login.html")

@login_required
def register_user(request):

    # If student profile already exists
    if hasattr(request.user, "student"):
        return redirect("dashboard")

    if request.method == "POST":
        email = request.POST.get("email")
        semester = request.POST.get("semester")
        phone_number = request.POST.get("phone_number")
        gender = request.POST.get("gender")
        college = request.POST.get("college")

        # Basic required field check
        if not all([email, semester, phone_number, gender, college]):
            return render(request, "student/create.html", {
                "error": "All fields are required."
            })

        # Email uniqueness check
        if Student.objects.filter(email=email).exists():
            return render(request, "student/create.html", {
                "error": "Email already registered."
            })

        # Create student profile
        Student.objects.create(
            user=request.user,
            email=email,
            semester=semester,
            phone_number=phone_number,
            gender=gender,
            college=college
        )

        return redirect("dashboard")

    return render(request, "student/create.html")
@login_required
def student_profile(request):
    student = get_object_or_404(Student, user=request.user)
    return render(request, "student/student_profile.html", {
        "student": student
    })
@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("dashboard")
@login_required
def update_user(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("student_profile")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "student/update_user.html", {"form": form})
@login_required
def update_student(request):
    student = Student.objects.get(user=request.user)

    if request.method == "POST":
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_profile")
    else:
        form = StudentUpdateForm(instance=student)

    return render(request, "student/update_student.html", {"form": form})