from django import forms 
from .models import Leaves
class CreateLeavesForm(forms.ModelForm):
    class Meta:
        model = Leaves
        fields = [
            "reason",
            "place_on_leave",
            "date_to_leave",
            "date_of_return",
        ]
