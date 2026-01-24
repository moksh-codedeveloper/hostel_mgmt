from django.db import models
from students.models import Student
# Create your models here.

class Complaint(models.Model):
    ATTENTION_LEVEL = [
        ("I", "Immediate"),
        ("H", "High"),
        ("M", "Medium")
    ]
    COMPLAINT_STATUS = [
        ("O", "Opened"),
        ("R", "Resolved"),
        ("U", "UnOpened"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField()
    status = models.CharField(max_length=1, choices=COMPLAINT_STATUS)
    attention_level = models.CharField(max_length=1, choices=ATTENTION_LEVEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.student.user.full_name} -> {self.status} -> {self.attention_level}"
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student"],
                name="unique_complaints_per_student"
            )
        ]