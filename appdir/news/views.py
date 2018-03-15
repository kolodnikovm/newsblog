from django.db.models import Count
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

import news.serializers
from news.filters import NewsFilter, TagsFilterBackend
from news.models import Author, Category, News, Tag
from users.models import User


class NewsViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = news.serializers.NewsSerializer
    filter_class = NewsFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter,
                       SearchFilter, TagsFilterBackend,)
    search_fields = ('text_content', 'category__name',
                     'tags__name' 'author__name')
    ordering_fields = ('creation_date', 'author__name', 'category__name')

    def list(self, request):
        queryset = self.filter_queryset(News.objects.filter(is_published=True))
        serializer = news.serializers.NewsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = News.objects.filter(is_published=True)
        a_news = get_object_or_404(queryset, pk=pk)
        serializer = news.serializers.NewsSerializer(a_news)
        return Response(serializer.data)

    @list_route()
    def get_drafts(self, request):
        if request.user.is_staff:
            queryset = News.objects.filter(is_published=False)
            serializer = news.serializers.NewsSerializer(queryset, many=True)
            return Response(serializer.data)

        return Response({'detail': 'There is definitely no such an API'}, status=status.HTTP_404_NOT_FOUND)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = news.serializers.CategorySerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = news.serializers.TagSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = news.serializers.AuthorSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = news.serializers.UserSerializer

    def list(self, request):
        if request.user.is_staff:
            queryset = self.get_queryset()
            serializer = news.serializers.UserSerializer(queryset, many=True)
            return Response(serializer.data)

        return Response({'detail': 'There is definitely no such an API'}, status=status.HTTP_404_NOT_FOUND)
