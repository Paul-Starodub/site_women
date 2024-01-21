from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
)
from django.shortcuts import render, get_object_or_404
from women.models import Women, Category, TagPost

menu = [
    {"title": "About site", "url_name": "women:about"},
    {"title": "Add an article", "url_name": "women:add_page"},
    {"title": "Feedback", "url_name": "women:contact"},
    {"title": "Enter", "url_name": "women:login"},
]


def index(request: HttpRequest) -> HttpResponse:
    posts = Women.published.select_related("cat")
    data = {
        "title": "women",
        "menu": menu,
        "posts": posts,
        "cat_selected": 0,
    }
    return render(request, "women/index.html", context=data)


def about(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "women/about.html",
        context={"title": "About site", "menu": menu},
    )


def show_post(request: HttpRequest, post_slug: str) -> HttpResponse:
    post = get_object_or_404(Women, slug=post_slug)
    data = {"title": post.title, "menu": menu, "post": post, "cat_selected": 1}
    return render(request, "women/post.html", context=data)


def addpage(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "women/addpage.html",
        context={"menu": menu, "title": "Add an article"},
    )


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Feedback")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Authorization")


def show_category(request: HttpRequest, cat_slug: str) -> HttpResponse:
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related("cat")
    data = {
        "title": f"Displaying category: {category.name}",
        "menu": menu,
        "posts": posts,
        "cat_selected": category.pk,
    }
    return render(request, "women/index.html", context=data)


def page_not_found(
    request: HttpRequest, exception: Exception
) -> HttpResponseNotFound:
    return HttpResponseNotFound("Page not found!!!")


def show_tag_postlist(request: HttpRequest, tag_slug: str) -> HttpResponse:
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(
        is_published=Women.Status.PUBLISHED
    ).select_related("cat")

    data = {
        "title": f"Tag: {tag.tag}",
        "menu": menu,
        "posts": posts,
        "cat_selected": 0,
    }

    return render(request, "women/index.html", context=data)
