from django.http import HttpRequest, HttpResponse, HttpResponseNotFound


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Women's page")


def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f"<h2>Category id:{cat_id}</h2>")


def categories_by_slug(request: HttpRequest, cat_slug: int) -> HttpResponse:
    return HttpResponse(f"<h2>Category slug:{cat_slug}</h2>")


def archive(request: HttpRequest, year: int) -> HttpResponse:
    return HttpResponse(f"<h2>Category year:{year}</h2>")


def page_not_found(
    request: HttpRequest, exception: Exception
) -> HttpResponseNotFound:
    return HttpResponseNotFound("Page not found!!!")
