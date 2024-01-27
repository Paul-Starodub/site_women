from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Login", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "password")


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Login", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
        labels = (
            {
                "email": "E-mail",
                "first_name": "First Name",
                "last_name": "Last Name",
            },
        )
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-input"}),
            "first_name": forms.TextInput(attrs={"class": "form-input"}),
            "last_name": forms.TextInput(attrs={"class": "form-input"}),
        }

    def clean_password2(self) -> str:
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Different passwords")
        return cd["password"]

    def clean_email(self) -> str:
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email
