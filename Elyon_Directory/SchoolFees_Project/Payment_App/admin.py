from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("receipt_number", "student", "amount_paid", "payment_method", "created_at")
    search_fields = ("student__name", "receipt_number", "transaction_reference")
    list_filter = ("payment_method", "created_at")
