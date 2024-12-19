from django.shortcuts import render
from usuarios.forms import LoginForms, SignupForms

def login (request):
    form = LoginForms()
    return render(request, "usuarios/login.html", {"form": form})

def signup(request):
    form = SignupForms()
    return render(request, "usuarios/signup.html", {"form": form})