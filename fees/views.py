from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Fees

@login_required
def fees_page(request):
    return render(request, "fees/fees.html")


@login_required
def fees_by_status(request):
    status = request.GET.get("status")

    if status not in ["P", "UP"]:
        return JsonResponse(
            {"error": "Invalid status. Use P or UP"},
            status=400
        )

    student = request.user.student
    fees = student.fees.filter(fees_status=status)

    data = [
        {
            "id": fee.id,
            "total_amount": str(fee.total_amount),
            "amount_paid": str(fee.amount_paid),
            "status": fee.fees_status,
            "created_at": fee.created_at
        }
        for fee in fees
    ]

    return JsonResponse({"fees": data}, status=200)
@login_required
def fees_history(request):
    student = request.user.student
    fees = student.fees.all().order_by("-created_at")
    data = [
        {
            "id": fee.id,
            "semester": fee.semester,
            "total_amount": str(fee.total_amount),
            "amount_paid": str(fee.amount_paid),
            "status": fee.fees_status,
            "created_at": str(fee.created_at.date()),
        }
        for fee in fees
    ]
    return JsonResponse({"fees": data}, status=200)

@login_required
def last_fee(request):
    student = request.user.student
    fee = student.fees.order_by("-created_at").first()
    if not fee:
        return JsonResponse({"message": "No fee records found"}, status=404)
    data = {
        "id": fee.id,
        "semester": fee.semester,
        "total_amount": str(fee.total_amount),
        "amount_paid": str(fee.amount_paid),
        "status": fee.fees_status,
        "is_fully_paid": fee.is_fully_paid,
        "created_at": str(fee.created_at.date()),
    }
    return JsonResponse({"fee": data}, status=200)