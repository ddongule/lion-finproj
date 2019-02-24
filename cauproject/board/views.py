from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def free_board(request):
  return render(request,'free_board.html')

def inquire(request):
  return render(request,'inquire.html')