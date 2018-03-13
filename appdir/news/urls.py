from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('authors', views.AuthorList.as_view()),
    path('tags', views.TagList.as_view()),
    path('categories', views.CategoryList.as_view()),
]
urlpatterns += router.urls
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]


