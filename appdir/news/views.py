from django.db.models import Count
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from news.filters import NewsFilter
from news.models import News, Tag
from news.permissions import IsOwnerOrReadOnly
from news.serializers import NewsSerializer, UserSerializer
from users.models import User


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_class = NewsFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)

    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        stags = self.request.query_params.get('stags', None)
        queryset = News.objects.all()
        if stags:
            stags = [int(tag) for tag in stags.split()]
            queryset = News.objects.annotate(
                count=Count('tags')).filter(count=len(stags))
            for tag_id in stags:
                queryset = queryset.filter(tags__pk=tag_id)
        elif tags:
            tags = [int(tag) for tag in tags.split()]
            queryset = News.objects.filter(tags__id__in=tags).distinct()

        return queryset


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_url_kwarg = 'news_id'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'
