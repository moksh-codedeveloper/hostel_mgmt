from django.urls import path
from .views import create_leave, get_all_leaves, get_leave_by_id

urlpatterns = [
    path("create/", create_leave),
    path("all/", get_all_leaves),
    path("<leave_id>/", get_leave_by_id),
]
