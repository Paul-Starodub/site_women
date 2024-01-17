from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Women's page")


def categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h2>categories</h2>")
