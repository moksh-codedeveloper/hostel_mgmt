from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Hello Django 👋",
        "project": "Hostel Management System",
        "status": "alive",
    })
