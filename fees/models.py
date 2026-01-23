from django.db import models
from students.models import Student
from django.core.validators import MinValueValidator
# Create your models here.
class Fees(models.Model):
    FEES_STATUS = [
        ("P", "Paid"),
        ("UP", "Unpaid"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="fees")
    fees_status = models.CharField(max_length=2, choices=FEES_STATUS)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_fully_paid(self):
        return self.amount_paid >= self.total_amount
    def save(self, *args, **kwargs):
        if self.amount_paid >= self.total_amount:
            self.fees_status = "P"
        else:
            self.fees_status = "UP"
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.student.user.full_name} -> {self.total_amount} -> {self.amount_paid} -> {self.fees_status}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student"],
                name="unique_fee_per_student"
            )
        ]