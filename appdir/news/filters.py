from django_filters import rest_framework as filters
from news.models import News


class NewsFilter(filters.FilterSet):
    heading = filters.CharFilter(name='heading', lookup_expr='iexact')
    creation_date = filters.DateFilter(
        name='creation_date', lookup_expr=['lte', 'gte', 'exact'])
    author = filters.CharFilter(name='author__name', lookup_expr='iexact')
    category = filters.CharFilter(
        name='category__name', lookup_expr='iexact')
    # TODO Tag Filters

    class Meta:
        model = News
        fields = ['heading']
