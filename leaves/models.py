from django.db import models
from students.models import Student 

# Create your models here.

class Leaves(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.CharField(max_length=300)
    place_on_leave = models.CharField(max_length=100)
    date_to_leave = models.DateField(auto_now_add=True)
    date_of_return = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)