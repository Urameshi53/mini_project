from django import forms 


class CommentForm(forms.Form):
    comment_text = forms.CharField(label="comment", widget=forms.Textarea
                    (attrs={'class':'form-control', 'name':'comment', 'placeholder':'Your Comment*'}))

class BlogForm(forms.Form):
    title = forms.CharField(max_length=200)
    #content = forms.CharField(widget=forms.Textarea(attrs={'class':'tinymce-editor'}))
    content = forms.CharField(widget=forms.Textarea)

class ReplyForm(forms.Form):
    content = forms.CharField(label="Reply", widget=forms.Textarea(attrs={'class':'form-control', 'name':'comment', 'placeholder':'Your reply'}))
    
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
