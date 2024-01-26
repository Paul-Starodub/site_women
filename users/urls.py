from django.urls import path

from users import views


urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]

app_name = "users"
