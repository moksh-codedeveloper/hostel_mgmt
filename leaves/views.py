import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import CreateLeavesForm

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
