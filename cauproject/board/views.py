from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post,Notice
from .form import PostPost, NoticePost

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

def free_board_detail(request,post_id):
  details = get_object_or_404(Post, pk = post_id)
  return render(request, 'free_board_detail.html',{'details':details})

def free_board_new(request):
  if request.method == 'POST':
    form = PostPost(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.pub_date = timezone.now()
      post.save()
      return redirect('free_board')
  else:
    form = PostPost()
    return render(request,'free_board_new.html',{'form':form})

def inquire(request):
  return render(request,'inquire.html')

def notice(request):
  notices = Notice.objects
  notices_list = Notice.objects.all()
  paginator = Paginator(notices_list,5)
  page = request.GET.get('page')
  pages = paginator.get_page(page)
  return render(request, 'notice.html',{'notices':notices, 'pages':pages})

def notice_detail(request,notice_id):
  details = get_object_or_404(Notice, pk = notice_id)
  return render(request, 'notice_detail.html',{'details':details})

def notice_new(request):
  if request.method == 'POST':
    form = NoticePost(request.POST)
    if form.is_valid():
      notice = form.save(commit=False)
      notice.pub_date = timezone.now()
      notice.save()
      return redirect('notice')
  else:
    form = NoticePost()
    return render(request,'notice_new.html',{'form':form})