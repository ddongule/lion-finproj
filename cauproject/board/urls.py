from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('about/',views.about,name="about"),
  path('free_board/',views.free_board,name="free_board"),
  path('inquire/',views.inquire,name="inquire"),
  path('notice/',views.notice,name='notice'),
]