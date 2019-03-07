from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  body = models.TextField()
  nickName = models.CharField(max_length=20, default = 'nick name')

  def __str__(self):
    return self.title
  
  def summary(self):
    return self.body[:100]
  
class Notice(models.Model):
  title = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  body = models.TextField()

  def __str__(self):
    return self.title
  
class Comment(models.Model):
  nickName = models.CharField(max_length=20, default = 'nick name')
  pub_date = models.DateTimeField(auto_now_add = True)
  body = models.CharField(max_length = 200)
  post_id = models.IntegerField()
  # post_id = models.ForeignKey(Post, on_delete = models.CASCADE)

  def __str__(self):
    return self.body