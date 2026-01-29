from django import forms
from complaints.models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            "title",
            "description",
            "status",
            "attention_level"
        ]

class UpdateStatusComplaint(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ["status"]