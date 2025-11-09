from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Creating Home View
def home(request: HttpRequest) -> HttpResponse:
    return render(request, "./todo_website/index.html")