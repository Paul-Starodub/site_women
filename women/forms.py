from django import forms
from women.models import Category, Husband


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(
        required=False, label="Status", initial=True
    )
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Categories",
        empty_label="Didn't choose anything",
    )
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(), required=False, empty_label="Single"
    )
