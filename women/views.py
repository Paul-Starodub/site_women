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


data_db = [
    {
        "id": 1,
        "title": "Angelina Jolie",
        "content": """Angelina Jolie</h1> (born Angelina Jolie [7], born Voight, formerly Jolie Pitt; born June 4, 1975, Los Angeles, California, USA) - American film, television and voice actress, film director, screenwriter, producer, fashion model, UN Goodwill Ambassador.
     Winner of an Oscar, three Golden Globe awards (the first actress in history to win the award three years in a row) and two Screen Actors Guild Awards.""",
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
    posts = Women.published.all()
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
    return HttpResponse("Adding an article")


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Feedback")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Authorization")


def show_category(request: HttpRequest, cat_slug: str) -> HttpResponse:
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)
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
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)

    data = {
        "title": f"Tag: {tag.tag}",
        "menu": menu,
        "posts": posts,
        "cat_selected": 0,
    }

    return render(request, "women/index.html", context=data)
