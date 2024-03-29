menu = [
    {"title": "About site", "url_name": "women:about"},
    {"title": "Add an article", "url_name": "women:add_page"},
    {"title": "Feedback", "url_name": "women:contact"},
]


class DataMixin:
    title_page = None
    cat_selected = None
    extra_context = {}

    def __init__(self) -> None:
        if self.title_page:
            self.extra_context["title"] = self.title_page

        if self.cat_selected is not None:
            self.extra_context["cat_selected"] = self.cat_selected

    def get_mixin_context(self, context: dict, **kwargs: dict) -> dict:
        context["cat_selected"] = None
        context.update(kwargs)
        return context
