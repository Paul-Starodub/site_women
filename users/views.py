from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from users.forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Login"}

    def get_success_url(
        self,
    ) -> (
        str
    ):  # if we want to use our url instead default, or use LOGIN_REDIRECT_URL in settings.py
        return reverse_lazy("women:home")


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))
