from typing import Optional

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from site_women import settings
from users.forms import (
    LoginUserForm,
    RegisterUserForm,
    ProfileUserForm,
    UserPasswordChangeForm,
)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Login"}

    def get_success_url(
        self,
    ) -> str:  # if we want to use our url instead default,
        # or use LOGIN_REDIRECT_URL in settings.py
        return reverse_lazy("women:home")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "Register"}
    success_url = reverse_lazy("users:login")


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "users/profile.html"
    extra_context = {
        "title": "User's profile",
        "default_image": settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self) -> str:
        return reverse_lazy("users:profile")

    def get_object(self, queryset=None) -> Optional[User]:
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
