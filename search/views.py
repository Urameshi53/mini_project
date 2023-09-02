from django.shortcuts import render
from django.views import generic
from .forms import SearchForm
from django.utils import timezone


from blogs.models import Blog

# Create your views here.

class SearchView(generic.TemplateView):
    template_name = "search/search.html"


def search_view(request):
    form = SearchForm(request.GET)
    results = []
    latest = Blog.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    popular = Blog.objects.filter(pub_date__lte=timezone.now()).order_by("likes")[:5]
    trending = Blog.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Blog.objects.filter(title__icontains=query)  # Replace 'some_field' with the field you want to search in.

    return render(request, 'search/search.html', {'form':form, 'results': results, 'latest':latest, 'popular':popular, 'trending':trending})
    
