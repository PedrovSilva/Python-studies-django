from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Jaum Silva"
            }
        ),
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                 "placeholder": "Digite sua senha"
            }
        )
    )

class SignupForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Jaum Silva"
            }
        ),
    )
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
             attrs={
                "class": "form-control",
                "placeholder": "Ex.: saumsilva@mailcom"
            }
        )    
    )
    senha_1=forms.CharField(
        label="Repita sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                 "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                 "placeholder": "Digite sua senha novamente"
            }
        )
    )