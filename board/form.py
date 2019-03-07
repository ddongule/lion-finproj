from django import forms
from .models import Post,Notice,Comment

class PostPost(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title','body','nickName']

class NoticePost(forms.ModelForm):
  class Meta:
    model = Notice
    fields = ['title','body']

class CommentPost(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['nickName','body']