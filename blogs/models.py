from django.db import models
from django.contrib.auth.models import User
from django.forms import DateInput, ModelForm
from django import forms
from django.utils.timezone import now


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(blank=True, default=now)
    title = models.CharField(max_length=200)
    content = models.TextField()
    likes = models.IntegerField()
    CATEGORY_CHOICES = [
        ("GR", "General"),
        ("LS", "LifeStyle"),
        ("TR", "Travel"),
        ("DS", "Design"),
        ("CR", "Creative"),
        ("ED", "Education"),
    ]
    category = models.CharField(blank=True, default="GR", max_length=2, choices=CATEGORY_CHOICES)
    tag = models.CharField(max_length=12)
    back_img = models.ImageField(blank=True, upload_to="images", default='images/597_1.jpg')

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
    comment_text = models.TextField()

    def __str__(self) -> str:
        return self.comment_text

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
    content = models.CharField(max_length=240)

    def __str__(self) -> str:
        return self.content

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ["content"]

    
class CommentForm(ModelForm):
    class Meta:
        model = Comment 
        fields = ["comment_text"]

    '''def __init__(self, *args, **kwargs):
        super(CommentForm,self).__init__(*args, **kwargs)
        self.fields['pub_date'].widget = forms.DateInput(attrs={ 'type': 'date'})'''

class BlogForm(ModelForm):
    class Meta:
        model = Blog 
        fields = ["title", "content", "likes", "tag", "back_img"]


