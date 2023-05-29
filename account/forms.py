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
                "placeholder": "ឈ្មោះ​ពេញ",
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
                "placeholder": "លេខទូរសព្ទ",
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
                "placeholder": "អ៊ីមែល",
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
                "placeholder": "ឈ្មោះ​អ្នកប្រើប្រាស់",
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
                "placeholder": "ពាក្យសម្ងាត់",
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
                "placeholder": "បញ្ជាក់ពាក្យសម្ងាត់",
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
            attrs={"type": "email", "class": "form-control", "placeholder": "អ៊ីមែល"}
        ),
        label="អ៊ីមែល",
        required=True,
    )
    password = forms.CharField(
        max_length=30,
        min_length=6,
        label="ពាក្យសម្ងាត់",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "ពាក្យសម្ងាត់",
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
                raise forms.ValidationError(
                    "ឈ្មោះអ្នកប្រើ និងពាក្យសម្ងាត់មិនត្រឹមត្រូវ"
                )
