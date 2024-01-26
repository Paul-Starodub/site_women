from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def login_user(request: HttpRequest) -> HttpResponse:
    return HttpResponse("login")


def logout_user(request: HttpRequest) -> HttpResponse:
    return HttpResponse("logout")
