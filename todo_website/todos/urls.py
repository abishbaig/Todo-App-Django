from django.urls import path
from . import views

urlpatterns = [
    path("", views.todos_home, name="Todos"),
    path("<int:task_id>/completetask", views.complete_task, name="Complete_Task"),
    path("<int:task_id>/updatetask", views.update_task, name="Update_Task"),
    path("<int:task_id>/deletetask", views.delete_task, name="Delete_Task"),
    path('<int:task_id>/getform', views.get_edit_form, name='Get_Edit_Form'),
]
