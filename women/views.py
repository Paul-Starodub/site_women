from django.db.models import QuerySet
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
)
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

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


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = "women/addpage.html"
    extra_context = {"title": "Add Page", "menu": menu}


class UpdatePage(UpdateView):
    model = Women
    fields = ["title", "content", "photo", "is_published", "cat"]
    template_name = "women/addpage.html"
    success_url = reverse_lazy("women:home")
    extra_context = {"title": "Edit Page", "menu": menu}


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
