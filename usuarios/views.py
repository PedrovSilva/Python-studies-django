from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, SignupForms
from django.contrib.auth.models import User

def login (request):
    form = LoginForms()
    return render(request, "usuarios/login.html", {"form": form})

def signup(request):
    form = SignupForms()

    if request.method == "POST":
        form = SignupForms(request.POST)

        
        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect("signup")
            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
               return redirect("signup")
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect("login")

    return render(request, "usuarios/signup.html", {"form": form})