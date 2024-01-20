from django.contrib import admin

from women.models import Women


class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "is_published")


admin.site.register(Women, WomenAdmin)
