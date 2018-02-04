from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users', views.UserList.as_view()),
    path('users/<int:user_id>', views.UserDetail.as_view()),
    path('news/', views.NewsList.as_view()),
    path('news/<int:news_id>', views.NewsDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
