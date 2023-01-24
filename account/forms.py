from django import forms
from django.contrib.auth import get_user_model

# from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class RegisterForm(UserCreationForm):
    """
    The default

    """

    fullname = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Fullname",
                "autocomplete": False,
            }
        ),
        label=" ",
        required=True,
    )
    phone = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "class": "form-control",
                "placeholder": "Phone Number",
                "autocomplete": False,
            }
        ),
        label=" ",
        required=True,
    )
    email = forms.EmailField(
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "placeholder": "Email",
                "autocomplete": False,
            }
        ),
        label=" ",
        required=True,
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Username",
                "autocomplete": False,
            }
        ),
        label=" ",
        required=True,
    )

    password1 = forms.CharField(
        max_length=30,
        min_length=6,
        label=" ",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "autocomplete": False,
            }
        ),
    )
    password2 = forms.CharField(
        max_length=30,
        min_length=6,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Comfirm Password",
                "class": "form-control",
                "autocomplete": False,
            }
        ),
    )

    class Meta:
        model = User
        fields = ["email", "username", "fullname", "password1", "password2", "phone"]


class LoginForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=80,
        widget=forms.TextInput(
            attrs={"type": "email", "class": "form-control", "placeholder": "Email"}
        ),
        label="Email",
        required=True,
    )
    password = forms.CharField(
        max_length=30,
        min_length=6,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            if not authenticate(
                email=self.cleaned_data["email"], password=self.cleaned_data["password"]
            ):
                raise forms.ValidationError("Invalid Username and Password")
