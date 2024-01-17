from django.urls import path, re_path

from women import views

urlpatterns = [
    path("", views.index, name="women"),
    path("cats/<int:cat_id>/", views.categories, name="category"),
    path(
        "cats/<slug:cat_slug>/",
        views.categories_by_slug,
        name="category_by_slug",
    ),
    re_path(r"archive/(?P<year>[0-9]{4}/)", views.archive, name="archive"),
]

app_name = "women"
