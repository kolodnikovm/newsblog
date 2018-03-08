from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users', views.UserList.as_view()),
    path('news/', views.NewsList.as_view()),
    path('news/<int:news_id>', views.NewsDetail.as_view()),
    path('authors', views.AuthorList.as_view()),
    path('tags', views.TagList.as_view()),
    path('categories', views.CategoryList.as_view()),
    path('register', views.UserCreate.as_view(), name='register'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
