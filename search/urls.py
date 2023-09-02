from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from . import views 

app_name = "search"

urlpatterns = [
    path("", views.search_view, name="search"),
    #path("", views.SearchView.as_view(), name="search"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
