from django.db import models
from students.models import Student 

# Create your models here.

class Leaves(models.Model):
    STATUS = [
        ("A", "Approved"),
        ("P", "Pending"),
        ("R", "Rejected")
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name="leaves")
    reason = models.CharField(max_length=300)
    place_on_leave = models.CharField(max_length=100)
    date_to_leave = models.DateField()
    date_of_return = models.DateField()
    leave_status = models.CharField(max_length=1, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)