from django.contrib import admin
from django.urls import path
from quiz.views import quiz_view

urlpatterns = [
    path('admin/', admin.site.urls),  # 後台管理網址
    path('quiz/', quiz_view),         # 前台測驗網址
]