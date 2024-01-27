from django.contrib.auth.views import LogoutView
from django.urls import path

from users import views


urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

app_name = "users"
