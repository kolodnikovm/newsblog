from django.db.models import Count
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import generics, permissions, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

import news.serializers as n_serials
from news.filters import NewsFilter
from news.models import Author, Category, DraftNews, PublishedNews, Tag
from news.permissions import IsOwnerOrReadOnly
from users.models import User


class NewsList(generics.ListCreateAPIView):
    queryset = PublishedNews.objects.all()
    serializer_class = n_serials.PublishedNewsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = NewsFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend, SearchFilter)
    ordering_fields = ('creation_date', 'author__name', 'category__name',)
    search_fields = ('author__name', 'category__name',
                     'text_content', 'heading', 'tags__name')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)

    def get_queryset(self):
        """
        Custom queries on tags:
            -tags = <tag_id1>+<tag_id2>+...+<tag_id(n)> – news contain any given tags
            -stags = <tag_id1>+<tag_id2>+...+<tag_id(n)> – news contain exact set of tags
        """
        tags = self.request.query_params.get('tags', None)
        stags = self.request.query_params.get('stags', None)
        queryset = PublishedNews.objects.all()
        if stags:
            stags = [int(tag) for tag in stags.split()]
            queryset = PublishedNews.objects.annotate(
                count=Count('tags')).filter(count=len(stags))
            for tag_id in stags:
                queryset = queryset.filter(tags__pk=tag_id)
        elif tags:
            tags = [int(tag) for tag in tags.split()]
            queryset = PublishedNews.objects.filter(
                tags__id__in=tags).distinct()

        return queryset


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = n_serials.CategorySerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = n_serials.TagSerializer


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = n_serials.AuthorSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PublishedNews.objects.all()
    serializer_class = n_serials.PublishedNews
    lookup_url_kwarg = 'news_id'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = n_serials.UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.user
        if user.is_staff:
            return queryset

        raise Http404


class DraftNewsList(generics.ListAPIView):
    queryset = DraftNews.objects.all()
    serializer_class = n_serials.DraftNewsSerializer

    def get_queryset(self):
        queryset = DraftNews.objects.all()
        user = self.request.user
        if user.is_staff:
            return queryset

        raise Http404


class UserCreate(generics.CreateAPIView):
    serializer_class = n_serials.UserSerializer
