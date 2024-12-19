from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Username",
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
        label="Password",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                 "placeholder": "password"
            }
        )
    )

class SignupForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Username",
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
        label="Password",
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
        label="Retype your password",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                 "placeholder": "Digite sua senha novamente"
            }
        )
    )