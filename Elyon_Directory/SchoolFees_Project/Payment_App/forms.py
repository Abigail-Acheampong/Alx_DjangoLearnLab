from django import forms
from .models import Payment
from StudentInformation_App.models import StudentRecords

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["student", "amount_paid", "payment_method", "transaction_reference"]
        widgets = {
            "payment_method": forms.Select(choices=[
                ("Cash", "Cash"),
                ("Bank Transfer", "Bank Transfer"),
                ("Mobile Money", "Mobile Money"),
            ]),
            "student": forms.Select(attrs={"id": "student-dropdown"}),
        }
