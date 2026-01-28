from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import User, Student
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentUpdateForm, UserUpdateForm
@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({"message": "Method not allowed"}, status=405)

    data = json.loads(request.body)

    if User.objects.filter(username=data["username"]).exists():
        return JsonResponse({"message": "Username already exists"}, status=409)

    user = User.objects.create_user(
        username=data["username"],
        password=data["password"],
        full_name=data["full_name"]
    )

    login(request, user)

    return JsonResponse({
        "message": "User registered",
        "next": "/student/create/"
    }, status=201)
@csrf_exempt
def user_login(request):
    if request.method != "POST":
        return JsonResponse({"message": "Method not allowed"}, status=405)

    data = json.loads(request.body)

    user = authenticate(
        request=request,
        username=data["username"],
        password=data["password"]
    )

    if not user:
        return JsonResponse({"message": "Invalid credentials"}, status=403)

    login(request, user)

    if not hasattr(user, "student"):
        return JsonResponse({
            "message": "Profile incomplete",
            "next": "/student/create/"
        })

    return JsonResponse({
        "message": "Login successful",
        "next": "/dashboard"
    })

@csrf_exempt
@login_required
def register_user(request):
    if request.method != "POST":
        return JsonResponse({"message": "Method not allowed"}, status=405)

    if hasattr(request.user, "student"):
        return JsonResponse({"message": "Student already registered"}, status=409)
    REQUIRED_FIELD = [
        "gender",
        "semester", 
        "email", 
        "phone_number",
        "college"
    ]
    data = json.loads(request.body)
    
    for fields in REQUIRED_FIELD:
        if fields not in  data:
            return JsonResponse({
                "message" : "You do not have enough and required fields in the data passed as the json"
            })
    
    if Student.objects.filter(email=data["email"]).exists():
        return JsonResponse({
            "message" : "Do you really think i would not know you buddy you are same as always"
        })
    
    Student.objects.create(
        user = request.user,
        email= data["email"],
        semester=data["semester"],
        phone_number = data["phone_number"],
        gender = data["gender"],
        college = data["college"]
    )
    return JsonResponse({
        "message": "Student registered successfully"
    }, status=201)

@csrf_exempt
@login_required
def student_profile(request):
    if request.method != "GET":
        return JsonResponse({"message": "Method not allowed"}, status=405)

    if not hasattr(request.user, "student"):
        return JsonResponse(
            {"message": "Student profile not found"},
            status=404
        )

    student = request.user.student

    data = {
        "username": request.user.username,
        "full_name": request.user.full_name,
        "semester": student.semester,
        "college": student.college,
        "gender": student.gender,
        "email" : student.email,
        "phone_number" : student.phone_number
    }

    return JsonResponse(data, status=200)

@csrf_exempt
@login_required
def user_logout(request):
    if request.method != "POST":
        return JsonResponse({"message": "Method not allowed"}, status=405)

    logout(request)

    return JsonResponse({
        "message": "Logout successful",
        "next": "/user/login/"
    })

@csrf_exempt
@login_required
def update_student(request):
    if request.method != "POST":
        return JsonResponse({
            "message" : "Method not supported"
        })
    if not hasattr(request.user, "student"):
        return JsonResponse(
            {"message": "Student profile not found"},
            status=404
        )
    data = json.loads(request.body)
    user_form = UserUpdateForm(data, instance=request.user)
    student_form = StudentUpdateForm(data, instance=request.user.student)
    if not student_form.is_valid() or not user_form.is_valid():
        errors = {
            "student_errors": student_form.errors,
            "user_errors": user_form.errors,
        }
        return JsonResponse(errors, status=400)
    student_form.save()
    user_form.save()
    return JsonResponse({
        "message" : "Updated Successfully"
    }, status=200)