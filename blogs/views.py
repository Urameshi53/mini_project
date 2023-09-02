from typing import Any, Dict
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.core.paginator import Paginator


from .models import Blog, Comment, Reply, BlogForm
from .forms import CommentForm, ReplyForm, SearchForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = "blogs/index.html"
    context_object_name = "latest_blog_list"
    paginate_by = 3
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest'] = Blog.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
        return context

class DetailView(generic.DetailView):
    model = Blog 
    template_name = "blogs/details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context['blogs'] = Blog.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
        context['comments'] = Comment.objects.filter(blog_id=self.kwargs['pk'])#blog__pk=9)#context['blogs'].values('id'))
        context['replys'] = []
        
        all_replies = Reply.objects.all()
        for comment in context['comments']:
            for reply in all_replies:
                if reply.comment.comment_text == comment.comment_text:
                    context['replys'].append(reply)
        context['form_r'] = ReplyForm()
        context['form'] = CommentForm()
        context['search_form'] = SearchForm()
        return context
    
    
def createView(request):
    context = {}
    context['form'] = BlogForm()
    return render(request, "blogs/create.html", context)
    

def like(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.likes += 1

def createBlog(request):
    if request.method == 'POST':
        #request.POST['back_img'] = 'images/597_1.jpg'
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():     
            blog = form.save(commit=False)
            user = request.user 
            blog.author = user 
            blog.save()
        else:
            print(form.errors.as_data()) 
    return HttpResponseRedirect("/blogs/")
    
def post(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    new_comment = Comment()
    new_comment.comment_text = request.POST['comment_text']
    new_comment.pub_date = datetime.datetime.now()
    new_comment.author = request.user
    new_comment.blog_id = blog_id
    new_comment.save()
    blog.comment_set.add(new_comment)
    return HttpResponseRedirect(f"/blogs/{blog_id}/")

def reply(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    new_reply = Reply()
    new_reply.content = request.POST['content']
    new_reply.pub_date = datetime.datetime.now()
    new_reply.author = request.user
    comment.reply_set.add(new_reply)
    new_reply.save()
    comment.reply_set.add(new_reply)
    return HttpResponseRedirect(f"/blogs/")

    
def search(request):
    form = SearchForm(request.GET)
    results = []
    latest = Blog.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    popular = Blog.objects.filter(pub_date__lte=timezone.now()).order_by("likes")[:5]
    trending = Blog.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Blog.objects.filter(title__contains=query)
    
    return render(request, 'search/search.html', {'form':form, 'results': results, 'latest':latest, 'popular':popular, 'trending':trending})


