from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from . import views 

app_name = "blogs"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("home/", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:blog_id>/post/", views.post , name="post"),
    path("<int:blog_id>/reply/", views.post , name="reply"),
    path("create/", views.createView , name="create"),
    path("create/blog/", views.createBlog, name="createBlog")
]
