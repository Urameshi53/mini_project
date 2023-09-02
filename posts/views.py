from django.shortcuts import render
from typing import Any, Dict
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
import datetime


from .models import Post

# Create your views here.

class PostView(generic.ListView):
    template_name = "posts/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()
    

