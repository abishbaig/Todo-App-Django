from django.contrib import admin
from .models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "due_date", "priority"]
    search_fields = ["title", "user__username"]
    list_filter = ["completed", "priority"]
