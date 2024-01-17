from django.urls import path, register_converter

from women import views
from women import convertors


register_converter(convertors.FourDigitYearConverter, "year4")

urlpatterns = [
    path("", views.index, name="women"),
    path("cats/<int:cat_id>/", views.categories, name="category"),
    path(
        "cats/<slug:cat_slug>/",
        views.categories_by_slug,
        name="category_by_slug",
    ),
    path("archive/<year4:year>/", views.archive, name="archive"),
]

app_name = "women"
