from django.contrib.auth.models import User
from djongo import models

class Student(models.Model):
    BRANCH_CHOICES = [
        ("ARI", "Artificial Intelligence"),
        ("CSE", "Computer Science"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to built-in User
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES, default="CSE")

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.branch}"

