from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import User, Student
import json
from django.views.decorators.csrf import csrf_exempt

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

    data = json.loads(request.body)

    Student.objects.create(
        user=request.user,
        semester=data["semester"],
        college=data["college"],
        gender=data["gender"]
    )

    return JsonResponse({
        "message": "Student registered successfully",
        "next": "/dashboard"
    }, status=201)
