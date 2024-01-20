from django import template
from women.models import Category

register = template.Library()


@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected: int = 0) -> dict:
    cats_db = Category.objects.all()
    return {"cats": cats_db, "cat_selected": cat_selected}
