from django.urls import path

from women import views


urlpatterns = [
    path("", views.WomenHome.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("addpage/", views.AddPage.as_view(), name="add_page"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("post/<slug:post_slug>/", views.show_post, name="post"),
    path(
        "category/<slug:cat_slug>/",
        views.WomenCategory.as_view(),
        name="category",
    ),
    path("tag/<slug:tag_slug>/", views.TagPostList.as_view(), name="tag"),
]

app_name = "women"
