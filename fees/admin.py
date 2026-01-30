from django.contrib import admin
from .models import Fees

@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "total_amount",
        "amount_paid",
        "fees_status",
        "updated_at",
    )

    readonly_fields = (
        "fees_status",
        "created_at",
        "updated_at",
    )

    def has_delete_permission(self, request, obj=None):
        return False
