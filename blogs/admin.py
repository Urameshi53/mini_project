from django.contrib import admin

from .models import Blog, Comment, Reply

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class ReplyInline(admin.TabularInline):
    model = Reply 
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Reply)