from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth import login


# Create your views here.
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("Todos")
    else:
        form = UserRegistrationForm()
    return render(request, "./registration/register.html", {"form": form})
