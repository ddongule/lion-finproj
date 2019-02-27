from django import forms
from .models import Post,Notice

class PostPost(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title','body','nickName']

class NoticePost(forms.ModelForm):
  class Meta:
    model = Notice
    fields = ['title','body']