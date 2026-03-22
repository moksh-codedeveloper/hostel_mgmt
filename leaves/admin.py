from django.contrib import admin
from .models import Leaves

@admin.register(Leaves)
class LeavesAdmin(admin.ModelAdmin):
    list_display = ("get_student_name", "place_on_leave", "date_to_leave", "date_of_return", "leave_status", "created_at")
    list_filter = ("leave_status",)
    search_fields = ("student__user__full_name", "place_on_leave", "reason")
    ordering = ("-created_at",)

    # This is the key part — admin can change status directly from the list
    list_editable = ("leave_status",)

    readonly_fields = ("created_at", "updated_at")

    def get_student_name(self, obj):
        return obj.student.user.full_name
    get_student_name.short_description = "Student"