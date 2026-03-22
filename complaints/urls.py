from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path("", views.complaints_page, name="complaints_page"),
    path("create/", views.create_complaint_page, name="create_complaint_page"),
    # APIs
    path("list/", views.list_complaints, name="list_complaints"),
    path("create-api/", views.create_complain, name="create_complaint_api"),
    path("update/", views.update_status, name="update_complaint"),
    path("delete/<int:complaint_id>/", views.delete_complaint, name="delete_complaint"),
]