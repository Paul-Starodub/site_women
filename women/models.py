from django.db import models
from django.db.models import QuerySet
from django.template.defaultfilters import slugify
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return (
            super().get_queryset().filter(is_published=Women.Status.PUBLISHED)
        )


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Draft"
        PUBLISHED = 1, "Published"

    title = models.CharField(max_length=255, verbose_name="women title")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        default=None,
        blank=True,
        null=True,
        verbose_name="photo",
    )
    content = models.TextField(blank=True, verbose_name="Article")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.DRAFT,
        verbose_name="status",
    )
    cat = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="posts"
    )
    tags = models.ManyToManyField("TagPost", blank=True, related_name="tags")
    husband = models.OneToOneField(
        "Husband",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="woman",
    )

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Famous woman"
        verbose_name_plural = "Famous women"
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]

    def get_absolute_url(self) -> str:
        return reverse("women:post", kwargs={"post_slug": self.slug})


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name="Category"
    )
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self) -> str:
        return reverse("women:category", kwargs={"cat_slug": self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.tag

    def get_absolute_url(self) -> str:
        return reverse("women:tag", kwargs={"tag_slug": self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name


class UploadedFiles(models.Model):
    file = models.FileField(upload_to="uploads_model")
