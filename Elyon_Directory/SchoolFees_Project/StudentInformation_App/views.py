from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentRecords
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def register_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        admission_number = request.POST.get("admission_number")
        grade = request.POST.get("grade")
        guardian_name = request.POST.get("guardian_name")
        guardian_contact = request.POST.get("guardian_contact")

        student = StudentRecords.objects.create(
            registered_by=request.user,
            name=name,
            admission_number=admission_number,
            grade=grade,
            guardian_name=guardian_name,
            guardian_contact=guardian_contact
        )
        student.save()

        messages.success(request, f"Student {name} has been successfully registered!") 
        # return redirect("student_list")  # Update with the correct URL name

    return render(request, "StudentInformation_App/register_student.html")

@login_required
def student_list(request):
    students = StudentRecords.objects.all()  # Fetch all student records
    return render(request, "StudentInformation_App/student_list.html", {"students": students})

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(StudentRecords, id=student_id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.guardian_name = request.POST.get("guardian_name")
        student.guardian_contact = request.POST.get("guardian_contact")
        student.save()
        return redirect("student_list")  # Redirect to student list after saving

    return render(request, "StudentInformation_App/edit_student.html", {"student": student})