from django.db import models
from StudentInformation_App.models import StudentRecords

class Payment(models.Model):
    student = models.ForeignKey(StudentRecords, on_delete=models.CASCADE)  # Foreign Key to Student
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ("Cash", "Cash"),
        ("Bank Transfer", "Bank Transfer"),
        ("Mobile Money", "Mobile Money"),
    ])
    transaction_reference = models.CharField(max_length=50, unique=True)
    receipt_number = models.PositiveIntegerField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.receipt_number:
            last_payment = Payment.objects.order_by("-receipt_number").first()
            self.receipt_number = (last_payment.receipt_number + 1) if last_payment else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Receipt {self.receipt_number} - {self.student.name}"
