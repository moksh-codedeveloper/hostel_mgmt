from django.urls import path
from .views import create_leave, get_all_leaves, get_leave_by_id, leaves_page, create_leaves_page

urlpatterns = [
    path("create/", create_leaves_page, name="create_leaves_page"),
    path("create-api/", create_leave),
    path("all/", leaves_page, name="leaves_page"),           # page
    path("all/api/", get_all_leaves, name="leaves_api"),
    path("<leave_id>/", get_leave_by_id),
]
