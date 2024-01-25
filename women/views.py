from django.db.models import QuerySet
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
)
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from women.forms import AddPostForm, UploadFileForm
from women.models import Women, TagPost, UploadedFiles

menu = [
    {"title": "About site", "url_name": "women:about"},
    {"title": "Add an article", "url_name": "women:add_page"},
    {"title": "Feedback", "url_name": "women:contact"},
    {"title": "Enter", "url_name": "women:login"},
]


class WomenHome(ListView):
    template_name = "women/index.html"
    context_object_name = "posts"
    extra_context = {
        "title": "women",
        "menu": menu,
        "cat_selected": 0,
    }

    def get_queryset(self) -> QuerySet:
        return Women.published.select_related("cat")


def about(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadedFiles(file=form.cleaned_data["file"])
            fp.save()
    else:
        form = UploadFileForm()
    return render(
        request,
        "women/about.html",
        context={"title": "About site", "menu": menu, "form": form},
    )


class ShowPost(DetailView):
    model = Women
    template_name = "women/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["title"] = context["post"].title
        context["menu"] = menu
        return context

    def get_object(self, queryset=None) -> Women:
        return get_object_or_404(
            Women.published,
            slug=self.kwargs[
                self.slug_url_kwarg
            ],  # use manager instead published=True
        )


class AddPage(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = AddPostForm()
        data = {"menu": menu, "title": "Add an article", "form": form}

        return render(
            request,
            "women/addpage.html",
            context=data,
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("women:home")
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


class WomenCategory(ListView):
    template_name = "women/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self) -> QuerySet:
        return Women.published.filter(
            cat__slug=self.kwargs["cat_slug"]
        ).select_related("cat")

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        cat = context["posts"][0].cat
        context["title"] = "Category" + cat.name
        context["menu"] = menu
        context["cat_selected"] = cat.pk
        return context


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


class TagPostList(ListView):
    template_name = "women/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs["tag_slug"])
        context["title"] = "Tag: " + tag.tag
        context["menu"] = menu
        context["cat_selected"] = None
        return context

    def get_queryset(self) -> QuerySet:
        return Women.published.filter(
            tags__slug=self.kwargs["tag_slug"]
        ).select_related("cat")
