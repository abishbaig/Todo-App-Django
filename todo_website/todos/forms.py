from django import forms
from .models import Task


# Creating Task Form
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "priority"]
        widgets = {
            "due_date": forms.DateInput(format="%Y-%m-%d",attrs={'type':'date'}),
        }


