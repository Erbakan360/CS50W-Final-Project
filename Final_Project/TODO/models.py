from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Task(models.Model):
    A_IMPORTANT = "Important"
    B_HIGH_PRIORITY = "High priority"
    C_MEDIUM_PRIORITY = "Medium priority"
    D_LOW_PRIORITY = "Low priority"
    E_GENERAL = "General"

    CATEGORIES = [
        (A_IMPORTANT,"Important"),
        (B_HIGH_PRIORITY,"High priority"),
        (C_MEDIUM_PRIORITY,"Medium priority"),
        (D_LOW_PRIORITY,"Low priority"),
        (E_GENERAL,"General"),
    ]

    Task_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    Task_Title = models.CharField(max_length=50)
    Task_Content = models.CharField(max_length=500, blank=True)
    Task_Flag = models.CharField(max_length=50, choices=CATEGORIES,)
    start_time = models.DateTimeField(auto_now_add=True, blank=True)
    deadline = models.DateTimeField(auto_now_add=False, blank=True)
    Status = models.BooleanField(default=False)