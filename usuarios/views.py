from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, SignupForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login (request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form["nome_login"].value()
            senha=form["senha"].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} login")
            return redirect("index")
        else:
            messages.error(request, "Auth fail")
            return redirect("login")
    return render(request, "usuarios/login.html", {"form": form})

def signup(request):
    form = SignupForms()

    if request.method == "POST":
        form = SignupForms(request.POST)

        
        if form.is_valid():
          
            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
               messages.error(request, "User already exists")
               return redirect("signup")
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            messages.success(request, "User sign up succefully")
            usuario.save()
            return redirect("login")

    return render(request, "usuarios/signup.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Bye bye")
    return redirect("login")