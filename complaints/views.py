from .forms import ComplaintForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .forms import UpdateStatusComplaint
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from .models import Complaint
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

@login_required
def update_status(request):
    if request.method != "PUT":
        return JsonResponse(
            {"message": "Only PUT allowed"},
            status=405
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"message": "Invalid JSON"}, status=400)

    complaint = get_object_or_404(
        Complaint,
        student=request.user.student
    )

    form = UpdateStatusComplaint(data, instance=complaint)
    if not form.is_valid():
        return JsonResponse(
            {"errors": form.errors},
            status=400
        )

    form.save()
    return JsonResponse(
        {"message": "Status updated successfully"},
        status=200
    )


@login_required
def delete_complaint(request, complaint_id):
    if request.method != "DELETE":
        return JsonResponse(
            {"message": "Only DELETE method allowed"},
            status=405
        )

    # Get complaint that belongs to THIS student
    complaint = get_object_or_404(
        Complaint,
        id=complaint_id,
        student=request.user.student
    )
    if complaint.status == "U":
        return JsonResponse({"message": "Complaint is not even opened yet"}, status=403)
    # Check if complaint is resolved
    if complaint.status != "R":
        return JsonResponse(
            {"message": "Complaint must be resolved before deletion"},
            status=403
        )

    complaint.delete()

    return JsonResponse(
        {"message": "Complaint deleted successfully"},
        status=200
    )

@login_required
def list_complaints(request):
    if request.method != "GET":
        return JsonResponse({"message" : "This is not supported GET"}, status=405)
    complaint = Complaint.objects.filter(
        student=request.user.student
    ).values(
        "id",
        "title",
        "description",
        "status",
        "attention_level"
    )
    return JsonResponse({
        "message" : "This is the list of complaints",
        "complaints" : list(complaint)
    }, status=200)