from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Women's page")


def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f"<h2>Category id:{cat_id}</h2>")


def categories_by_slug(request: HttpRequest, cat_slug: int) -> HttpResponse:
    return HttpResponse(f"<h2>Category slug:{cat_slug}</h2>")


def archive(request: HttpRequest, year: int) -> HttpResponse:
    return HttpResponse(f"<h2>Category year:{year}</h2>")