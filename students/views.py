from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import User, Student
import json
# Create your views here.


def register(request):
    if request.method != "POST":
        return JsonResponse({"message" : "not supported METHOD"}, status=405)
    data = json.load(request.body)
    user = User.objects.create_user(
        username=data["username"],
        password=data["password"],
        full_name=data["full_name"]
    )
    login(request=request, user=user)
    return JsonResponse({
        "next" : "/students/register/"
    })

def user_login(request):
    if request.method != "POST":
        return JsonResponse({"message" : "not Supported METHOD"}, status=405)
    user = json.load(request.body)
    authenticated_user = authenticate(
        request=request,
        username= user["username"],
        password= user["password"]
    )
    if not authenticated_user:
        return JsonResponse({"message" : "Invalid Credentials"}, status=403)
    login(request, authenticated_user)
    return JsonResponse({"message" : "Login successful", "next" : "/dashboard"})
