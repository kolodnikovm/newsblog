from django_filters import rest_framework
from rest_framework import filters
from news.models import News, Tag
from django.db.models import Count


class NewsFilter(rest_framework.FilterSet):
    heading = rest_framework.CharFilter(name='heading', lookup_expr='iexact')
    creation_date = rest_framework.DateFilter(
        name='creation_date', lookup_expr=['lte', 'gte', 'exact'])
    author = rest_framework.CharFilter(
        name='author__name', lookup_expr='iexact')
    category = rest_framework.CharFilter(
        name='category__name', lookup_expr='iexact')

    class Meta:
        model = News
        fields = ['heading', 'creation_date', 'author', 'category']


class TagsFilterBackend(filters.BaseFilterBackend):
    """
    Filter tags.
    """

    def filter_queryset(self, request, queryset, view):
        tags = request.query_params.get('tags', None)
        stags = request.query_params.get('stags', None)
        result_queryset = queryset

        if stags:
            stags = [int(tag) for tag in stags.split()]
            result_queryset = queryset.annotate(
                count=Count('tags')).filter(count=len(stags))
            result_queryset = queryset.filter(
                tags=Tag.objects.filter(pk__in=stags))
            for tag_id in stags:
                result_queryset = result_queryset.filter(tags__pk=tag_id)
        elif tags:
            tags = [int(tag) for tag in tags.split()]
            result_queryset = queryset.filter(
                tags__id__in=tags).distinct()

        return result_queryset
