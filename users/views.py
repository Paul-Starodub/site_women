from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from users.forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Login"}

    def get_success_url(
        self,
    ) -> str:  # if we want to use our url instead default,
        # or use LOGIN_REDIRECT_URL in settings.py
        return reverse_lazy("women:home")
