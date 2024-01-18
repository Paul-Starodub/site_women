from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse


menu = ["about site", "add article", "feedback", "enter"]


data_db = [
    {
        "id": 1,
        "title": "Angelina Joly",
        "content": "Angelina's biography",
        "is_published": True,
    },
    {
        "id": 2,
        "title": "Margo Robby",
        "content": "Margo's biography",
        "is_published": False,
    },
    {
        "id": 3,
        "title": "July Roberts",
        "content": "July's biography",
        "is_published": True,
    },
]


def index(request: HttpRequest) -> HttpResponse:
    data = {
        "title": "women",
        "menu": menu,
        "posts": data_db,
    }
    return render(request, "women/index.html", context=data)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "women/about.html", context={"title": "About site"})


def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f"<h2>Category id:{cat_id}</h2>")


def categories_by_slug(request: HttpRequest, cat_slug: int) -> HttpResponse:
    return HttpResponse(f"<h2>Category slug:{cat_slug}</h2>")


def archive(request: HttpRequest, year: int) -> HttpResponse:
    if year > 2024:
        uri = reverse("women:category_by_slug", args=("music",))
        return HttpResponseRedirect(uri)
    return HttpResponse(f"<h2>Category year:{year}</h2>")


def page_not_found(
    request: HttpRequest, exception: Exception
) -> HttpResponseNotFound:
    return HttpResponseNotFound("Page not found!!!")
