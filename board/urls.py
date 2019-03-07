from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('about/',views.about,name="about"),
  path('free_board/',views.free_board,name="free_board"),
  path('free_board/<int:post_id>/',views.free_board_detail,name="free_board_detail"),
  path('free_board/new/',views.free_board_new,name="free_board_new"),
  path('inquire/',views.inquire,name="inquire"),
  path('notice/',views.notice,name='notice'),
  path('notice/<int:notice_id>/',views.notice_detail,name="notice_detail"),
  path('notice/new/',views.notice_new,name="notice_new"),
]