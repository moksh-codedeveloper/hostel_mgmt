from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect, render

def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "home.html")

def csrf_token(request):
    if request.method != "GET":
        return JsonResponse({
            "message" : "This is not supported"
        })
    return JsonResponse({"csrfToken": get_token(request)})
