from django.contrib import admin

from women.models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
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

    @admin.display(description="Short description", ordering="content")
    def brief_info(self, women: Women) -> str:
        return f"Description {len(women.content)} symbols"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
