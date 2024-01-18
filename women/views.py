from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse
from django.template.defaultfilters import slugify


menu = ["about site", "add article", "feedback", "enter"]


class MyClass:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b


def index(request: HttpRequest) -> HttpResponse:
    data = {
        "title": "women",
        "menu": menu,
        "float": 28.56,
        "lst": [1, 2, "abc", True],
        "set": {1, 2, 3, 2, 5},
        "dict": {"key_1": "value_1", "key_2": "value_2"},
        "obj": MyClass(10, 20),
        "url": slugify("The second page"),
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
