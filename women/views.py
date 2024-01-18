from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
)
from django.shortcuts import render


menu = [
    {"title": "About site", "url_name": "women:about"},
    {"title": "Add an article", "url_name": "women:add_page"},
    {"title": "Feedback", "url_name": "women:contact"},
    {"title": "Enter", "url_name": "women:login"},
]


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


def show_post(request: HttpRequest, post_id: int) -> HttpResponse:
    return HttpResponse(f"Displaying an article with id = {post_id}")


def addpage(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Adding an article")


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Feedback")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Authorization")


def page_not_found(
    request: HttpRequest, exception: Exception
) -> HttpResponseNotFound:
    return HttpResponseNotFound("Page not found!!!")
