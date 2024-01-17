from django.urls import path

from women import views

urlpatterns = [
    path("", views.index, name="women"),
    path("cats/", views.categories, name="categories"),
]

app_name = "women"
