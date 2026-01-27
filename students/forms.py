from django import forms
from .models import Student, User
class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "email", 
            "semester",
            "phone_number",
        ]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "full_name",
            "username",
        ]
