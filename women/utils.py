menu = [
    {"title": "About site", "url_name": "women:about"},
    {"title": "Add an article", "url_name": "women:add_page"},
    {"title": "Feedback", "url_name": "women:contact"},
    {"title": "Enter", "url_name": "women:login"},
]


class DataMixin:
    def get_mixin_context(self, context: dict, **kwargs: dict) -> dict:
        context["menu"] = menu
        context["cat_selected"] = None
        context.update(kwargs)
        return context
