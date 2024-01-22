import os
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
)
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

from women.forms import AddPostForm, UploadFileForm
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


def handle_uploaded_file(f: InMemoryUploadedFile) -> None:
    base_dir = settings.BASE_DIR
    upload_dir = os.path.join(base_dir, "uploads")

    # Create the 'uploads' directory if it doesn't exist
    os.makedirs(upload_dir, exist_ok=True)

    # Generate a unique filename using uuid
    unique_filename = str(uuid.uuid4()) + "_" + f.name
    file_path = os.path.join(upload_dir, unique_filename)

    with open(file_path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(
                f=form.cleaned_data["file"]
            )  # because `file` is written in forms.py
    else:
        form = UploadFileForm()
    return render(
        request,
        "women/about.html",
        context={"title": "About site", "menu": menu, "form": form},
    )


def show_post(request: HttpRequest, post_slug: str) -> HttpResponse:
    post = get_object_or_404(Women, slug=post_slug)
    data = {"title": post.title, "menu": menu, "post": post, "cat_selected": 1}
    return render(request, "women/post.html", context=data)


def addpage(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("women:home")
    else:
        form = AddPostForm()

    data = {"menu": menu, "title": "Add an article", "form": form}

    return render(
        request,
        "women/addpage.html",
        context=data,
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
