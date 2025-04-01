from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Payment
from .forms import PaymentForm
from StudentInformation_App.models import StudentRecords

def register_payment(request):
    form = PaymentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Payment recorded successfully!")
            return redirect("payment_list")
    
    return render(request, "Payment_App/register_payment.html", {"form": form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, "Payment_App/payment_list.html", {"payments": payments})

def get_students_by_grade(request):
    grade = request.GET.get("grade", "").strip()
    print(f"Grade received: {grade}")
    students = StudentRecords.objects.filter(grade=grade).values("id", "name")
    students_list = list(students)
    print(f"Students found: {students_list}")  # Debugging print
    return JsonResponse(list(students), safe=False)
