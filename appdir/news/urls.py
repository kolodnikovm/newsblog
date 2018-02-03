from django.urls import path, include

from . import views

urlpatterns = [
    path('news/<int:news_id>', views.news_detail),
]
