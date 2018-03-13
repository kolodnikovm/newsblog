from django_filters import rest_framework as filters
from news.models import News, Tag
from rest_framework import filters as filts
from django.http import Http404

class NewsFilter(filters.FilterSet):
    heading = filters.CharFilter(name='heading', lookup_expr='iexact')
    creation_date = filters.DateFilter(
        name='creation_date', lookup_expr=['lte', 'gte', 'exact'])
    author = filters.CharFilter(name='author__name', lookup_expr='iexact')
    category = filters.CharFilter(
        name='category__name', lookup_expr='iexact')

    class Meta:
        model = News
        fields = ['heading', 'creation_date', 'author', 'category']

class TagsFilterBackend(filts.BaseFilterBackend):
    """
    Filter tags.
    """
    def filter_queryset(self, request, queryset, view):
        tags = self.request.query_params.get('tags', None)
        stags = self.request.query_params.get('stags', None)

        if stags:
            stags = [int(tag) for tag in stags.split()]
            result_queryset = queryset.objects.annotate(
                count=Count('tags')).filter(count=len(stags))
            for tag_id in stags:
                result_queryset = result_queryset.filter(tags__pk=tag_id)
        elif tags:
            tags = [int(tag) for tag in tags.split()]
            result_queryset = queryset.objects.filter(
                tags__id__in=tags).distinct()

        return result_queryset

class isAdminFilterBackend(filts.BaseFilterBackend):
    pass