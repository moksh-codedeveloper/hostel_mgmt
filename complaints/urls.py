from django.urls import path
from .views import create_complain, delete_complaint, list_complaints, update_status
urlpatterns = [
    path("create/", create_complain, name="create_complaints"),
    path("update/", update_status,name="update_status"),
    path("delete/<complaint_id>/", delete_complaint,name="delete_complaint"),
    path("list/", list_complaints, name="list_complaints")
]
