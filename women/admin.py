from typing import Any, Tuple, List

from django.contrib import admin, messages
from django.db.models import QuerySet
from django.http import HttpRequest

from women.models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = "Woman status"
    parameter_name = "status"

    def lookups(
        self, request: HttpRequest, model_admin: Any
    ) -> List[Tuple[str, str]]:
        return [("married", "Married"), ("single", "Single")]

    def queryset(self, request: HttpRequest, queryset: QuerySet) -> QuerySet:
        if self.value() == "married":
            return queryset.filter(husband__isnull=False)
        if self.value() == "single":
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ("title", "content", "slug", "cat", "husband", "tags")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)  # filter_vertical
    list_display = (
        "title",
        "time_create",
        "is_published",
        "cat",
        "brief_info",
    )
    list_display_links = ("title",)
    ordering = ("-time_create", "title")
    list_editable = ("is_published",)
    list_per_page = 5
    actions = ["set_published", "set_unpublished"]
    search_fields = ("title__startswith", "cat__name")
    list_filter = ("cat__name", "is_published", MarriedFilter)

    @admin.display(description="Short description", ordering="content")
    def brief_info(self, women: Women) -> str:
        return f"Description {len(women.content)} symbols"

    @admin.action(description="Publish")
    def set_published(self, request: HttpRequest, queryset: QuerySet) -> None:
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Changed {count} articles")

    @admin.action(description="Unpublish")
    def set_unpublished(
        self, request: HttpRequest, queryset: QuerySet
    ) -> None:
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(
            request, f"Unpublished {count} articles", messages.WARNING
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
