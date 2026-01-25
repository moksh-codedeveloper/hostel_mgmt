from django import forms
from .models import Student

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["semester", "college", "gender"]
