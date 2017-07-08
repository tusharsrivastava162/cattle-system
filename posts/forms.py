from django import forms
from posts.models import Post, Comment

class PostForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'w3-input', 'required':'true', 'placeholder':'Add a title'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'class':'w3-input', 'required':'true', 'placeholder':'Add content'}))

    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'class':'w3-input', 'placeholder':'Add a comment...'}))

    class Meta:
        model = Comment
        fields = ['content']
