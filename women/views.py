from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.db.models import QuerySet
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.paginator import Paginator

from women.forms import AddPostForm
from women.models import Women, TagPost
from women.utils import DataMixin


class WomenHome(DataMixin, ListView):
    template_name = "women/index.html"
    context_object_name = "posts"
    title_page = "women"
    cat_selected = 0
    paginate_by = 3

    def get_queryset(self) -> QuerySet:
        return Women.published.select_related("cat")


@login_required()
def about(request: HttpRequest) -> HttpResponse:
    contact_list = Women.published.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "women/about.html",
        context={"title": "About site", "page_obj": page_obj},
    )


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = "women/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context["post"].title)

    def get_object(self, queryset=None) -> Women:
        return get_object_or_404(
            Women.published,
            slug=self.kwargs[
                self.slug_url_kwarg
            ],  # use manager instead published=True
        )


class AddPage(
    PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView
):
    form_class = AddPostForm
    template_name = "women/addpage.html"
    title_page = "Adding an article"
    permission_required = "women.add_women"  # <app>.<action>_<table>

    def form_valid(self, form: AddPostForm) -> HttpResponseRedirect:
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePage(PermissionRequiredMixin, DataMixin, UpdateView):
    model = Women
    fields = ["title", "content", "photo", "is_published", "cat"]
    template_name = "women/addpage.html"
    success_url = reverse_lazy("women:home")
    title_page = "Editing an article"
    permission_required = "women.change_women"


@permission_required(perm="women.view_women", raise_exception=True)
def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Feedback")


class WomenCategory(DataMixin, ListView):
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
        return self.get_mixin_context(
            context, title="Category" + cat.name, cat_selected=cat.pk
        )


def page_not_found(
    request: HttpRequest, exception: Exception
) -> HttpResponseNotFound:
    return HttpResponseNotFound("Page not found!!!")


class TagPostList(DataMixin, ListView):
    template_name = "women/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs["tag_slug"])
        return self.get_mixin_context(context=context, title="Tag: " + tag.tag)

    def get_queryset(self) -> QuerySet:
        return Women.published.filter(
            tags__slug=self.kwargs["tag_slug"]
        ).select_related("cat")
