import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import CreateLeavesForm
from .models import Leaves
from django.shortcuts import render

@login_required
def create_leave(request):
    if request.method != "POST":
        return JsonResponse(
            {"message": "This method is not available"},
            status=405
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {"message": "Invalid JSON"},
            status=400
        )

    form = CreateLeavesForm(data)

    if not form.is_valid():
        return JsonResponse(
            {"errors": form.errors},
            status=400
        )

    leave = form.save(commit=False)
    leave.student = request.user.student   # 🔥 correct place
    leave.save()

    return JsonResponse(
        {"message": "Leave created successfully"},
        status=201
    )
@login_required
def get_all_leaves(request):
    leaves = Leaves.objects.filter(student=request.user.student)
    data = [
        {
            "id": leave.pk,
            "reason": leave.reason,
            "place_on_leave": leave.place_on_leave,
            "status": leave.leave_status,
            "from": str(leave.date_to_leave),    # ← str() fixes it
            "to": str(leave.date_of_return),      # ← str() fixes it
        }
        for leave in leaves
    ]
    return JsonResponse({"leaves": data})

@login_required
def get_leave_by_id(request, leave_id):
    try:
        leave = Leaves.objects.get(
            id=leave_id,
            student=request.user.student
        )
    except Leaves.DoesNotExist:
        return JsonResponse(
            {"message": "Leave not found"},
            status=404
        )

    return JsonResponse({
        "reason": leave.reason,
        "status": leave.leave_status,
        "from": leave.date_to_leave,
        "to": leave.date_of_return,
    })

@login_required
def leaves_page(request):
    return render(request, "leaves/list.html")
@login_required
def create_leaves_page(request):
    return render(request,"leaves/create.html")