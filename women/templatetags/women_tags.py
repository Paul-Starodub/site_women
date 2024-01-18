from typing import List, Any
from django import template
import women.views as views


register = template.Library()


@register.simple_tag()
def get_categories() -> List[Any]:
    return views.cats_db


@register.inclusion_tag("women/list_categories.html")
def show_categories() -> dict:
    cats_db = views.cats_db
    return {"cats": cats_db}
