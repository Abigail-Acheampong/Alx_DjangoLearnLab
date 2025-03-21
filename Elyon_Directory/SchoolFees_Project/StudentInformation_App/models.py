from django.db import models
from django.contrib.auth.models import User  

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    admission_number = models.IntegerField(unique=True)
    grade = models.CharField(max_length=50)
    guardian_contact = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key reference to User model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
