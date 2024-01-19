from django.db import models
from django.db.models import QuerySet
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_published=True)


class Women(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]

    def get_absolute_url(self) -> str:
        return reverse("women:post", kwargs={"post_slug": self.slug})
