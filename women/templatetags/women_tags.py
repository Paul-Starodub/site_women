from typing import List, Any
from django import template
import women.views as views


register = template.Library()


@register.simple_tag()
def get_categories() -> List[Any]:
    return views.cats_db
