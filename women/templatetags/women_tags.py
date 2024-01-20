from django import template
from django.db.models import Count

from women.models import Category, TagPost

register = template.Library()


@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected: int = 0) -> dict:
    cats_db = Category.objects.annotate(total=Count("posts")).filter(
        total__gt=0
    )
    return {"cats": cats_db, "cat_selected": cat_selected}


@register.inclusion_tag("women/list_tags.html")
def show_all_tags() -> dict:
    return {
        "tags": TagPost.objects.annotate(total=Count("tags")).filter(
            total__gt=0
        )
    }
