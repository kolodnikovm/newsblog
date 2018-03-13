from django.db.models import Count
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import news.serializers as news_serials
from news.filters import NewsFilter, TagsFilterBackend
from news.models import Author, Category, News, Tag
from news.permissions import IsOwnerOrReadOnly
from users.models import User
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status

class NewsViewSet(mixins.ListModelMixin, 
                  mixins.RetrieveModelMixin, 
                  viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = news_serials.NewsSerializer
    filter_class = NewsFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter, TagsFilterBackend)
    search_fields = ('text_content', 'category__name', 'tags__name' 'author__name')
    ordering_fields = ('creation_date', 'author__name', 'category__name')
    
    def list(self, request):
        queryset = News.objects.filter(is_published=True)
        serializer = news_serials.NewsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = News.objects.all()
        news = get_object_or_404(queryset, pk=pk)
        serializer = news_serials.NewsSerializer(news)
        return Response(serializer.data)

    @list_route()
    def get_drafts(self, request):
        if request.user.is_staff:
            queryset = News.objects.filter(is_published=False)
            serializer = news_serials.NewsSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            raise Http404
        

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = news_serials.CategorySerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = news_serials.TagSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = news_serials.AuthorSerializer


class UserViewSet(mixins.ListModelMixin, 
                  mixins.CreateModelMixin, 
                  viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = news_serials.UserSerializer


    def list(self, request):
        if request.user.is_staff:
            queryset = self.get_queryset()
            serializer = news_serials.UserSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            raise Http404

    def create(self, request, *args, **kwargs):
        super().create(self, request, *args, **kwargs)


