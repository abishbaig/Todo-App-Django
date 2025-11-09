from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

# Create your views here.
# Todos of All Users Home Page
@login_required
def todos_home(request: HttpRequest) -> HttpResponse:
    all_tasks = Task.objects.filter(user=request.user)

    form_edit = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("Todos")
    else:
        form = TaskForm()
    context = {
        "tasks": all_tasks,
        "form": form,
        "form_edit":form_edit,
    }

    return render(request, "./todos/index.html", context)


# Complete or Uncomplete a Task based on Task and User ID
def complete_task(request: HttpRequest, task_id: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("Todos")


# Delete A Task
def delete_task(request: HttpRequest, task_id: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("Todos")
    return render(request, "./todos/index.html")


# Update/Edit Task
def update_task(request: HttpRequest, task_id: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        form_edit = TaskForm(request.POST, instance=task)
        if form_edit.is_valid():
            form_edit.save()
            return redirect("Todos")
    else:
        form_edit = TaskForm(instance=task)
    return render(request, "./todos/index.html", {"form_edit": form_edit})


def get_edit_form(request: HttpRequest, task_id: int) -> HttpResponse:
    """Fetches and renders the pre-populated edit form for a task."""
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    
    # Initialize the form with the instance data
    form_edit = TaskForm(instance=task)
    
    # Render a small template snippet (we'll create this next)
    html_form = render_to_string(
        './todos/snippets/edit_form_snippet.html', 
        {
            'form_edit': form_edit, 
            'task_id': task_id # Pass the ID for the form action URL
        }, 
        request=request
    )
    
    # Return the HTML content to the frontend
    return JsonResponse({'html_form': html_form})


