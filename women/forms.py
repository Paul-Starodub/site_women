from django import forms
from django.core.exceptions import ValidationError

from women.models import Category, Husband, Women


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Categories",
        empty_label="Didn't choose anything",
    )
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(), required=False, empty_label="Single"
    )

    class Meta:
        model = Women
        fields = [
            "title",
            "slug",
            "content",
            "photo",
            "is_published",
            "cat",
            "husband",
            "tags",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(attrs={"cols": 50, "rows": 5}),
        }
        labels = {"slug": "URL"}

    def clean_title(self) -> str:
        title = self.cleaned_data["title"]
        if len(title) > 50:
            raise ValidationError("Title is too long")
        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label="File")
