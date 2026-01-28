from django.http import JsonResponse
from django.middleware.csrf import get_token

def home(request):
    return JsonResponse({
        "message": "Hello Django 👋",
        "project": "Hostel Management System",
        "status": "alive",
    })

def csrf_token(request):
    if request.method != "GET":
        return JsonResponse({
            "message" : "This is not supported"
        })
    return JsonResponse({"csrfToken": get_token(request)})
