from .forms import ComplaintForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

@login_required
def create_complain(request):
    if request.method != "POST":
        return JsonResponse({"message": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"message": "Invalid JSON"}, status=400)

    form = ComplaintForm(data)
    if not form.is_valid():
        return JsonResponse({
            "errors": form.errors
        }, status=400)

    complaint = form.save(commit=False)
    complaint.student = request.user.student
    complaint.save()

    return JsonResponse({
        "message": "Complaint created successfully"
    }, status=201)
