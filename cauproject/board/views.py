from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post,Notice

# Create your views here.
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def free_board(request):
  posts = Post.objects
  posts_list = Post.objects.all()
  paginator = Paginator(posts_list,5)
  page = request.GET.get('page')
  pages = paginator.get_page(page)
  return render(request,'free_board.html',{'posts':posts,'pages':pages})

def inquire(request):
  return render(request,'inquire.html')

def notice(request):
  notices = Notice.objects
  notices_list = Notice.objects.all()
  paginator = Paginator(notices_list,5)
  page = request.GET.get('page')
  pages = paginator.get_page(page)
  return render(request, 'notice.html',{'notices':notices, 'pages':pages})