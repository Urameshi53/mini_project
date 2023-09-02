from django.db import models
from django.contrib.auth.models import User
from django.forms import DateInput, ModelForm
from django import forms

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content_img = models.ImageField(upload_to="images", default="images/d4c602d1d4891bd7309ce73f1cd5bea1.jpg")
    content_vid = models.FileField(upload_to="videos", default="videos/910f499a76b1c0bc1e0f7bd0067fc2e6.jpg")
    content = models.CharField(max_length=120)
    user_comment = models.CharField(max_length=120, default="Nothing")
    likes = models.IntegerField()

    def __str__(self) -> str:
        return self.content
    

class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_post = models.ForeignKey('self',null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.CharField(max_length=240)
