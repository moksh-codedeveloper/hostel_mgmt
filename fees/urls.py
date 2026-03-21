from django.urls import path
from . import views

urlpatterns = [
    path("history/", views.fees_history, name="fees_history"),
    path("status/", views.fees_by_status, name="fees_by_status"),
    path("last/", views.last_fee, name="last_fee"),
    path("", views.fees_page, name="fees_page")
]
