from django import forms
from .models import Student, User
class StudentUpdateForm(forms.ModelForm):
    phone_number = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    semester = forms.IntegerField(required=False)
    class Meta:
        model = Student
        fields = [
            "email", 
            "semester",
            "phone_number",
        ]

class UserUpdateForm(forms.ModelForm):
    full_name = forms.CharField(required=False)
    username = forms.CharField(required=False)
    class Meta:
        model = User
        fields = [
            "full_name",
            "username",
        ]
