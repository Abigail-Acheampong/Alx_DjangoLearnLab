from django.urls import path
from .views import student_list, register_student, edit_student

urlpatterns = [
    path("students/", student_list, name="student_list"),
    path("register/", register_student, name="register_student"),
    path("students/edit/<int:student_id>/", edit_student, name="edit_student"),
]