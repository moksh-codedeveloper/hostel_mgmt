from django.urls import path
from .views import create_complain
urlpatterns = [
    path("create/", create_complain, name="create_complaints")
]
