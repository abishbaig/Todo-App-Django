from django.db import models
from django.conf import settings


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Task"
    )
    priority_choices = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    priority = models.CharField(choices=priority_choices, default="Medium")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} created {self.title[:20]}"
