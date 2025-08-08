import django_filters
from .models import Project

class ProjectFilter(django_filters.FilterSet):
    """
    项目过滤器
    """
    category = django_filters.CharFilter(field_name='category__slug')
    tag = django_filters.CharFilter(field_name='tags__slug')
    author = django_filters.CharFilter(field_name='author__username')
    start_date_after = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    start_date_before = django_filters.DateFilter(field_name='start_date', lookup_expr='lte')
    end_date_after = django_filters.DateFilter(field_name='end_date', lookup_expr='gte')
    end_date_before = django_filters.DateFilter(field_name='end_date', lookup_expr='lte')
    published_after = django_filters.DateTimeFilter(field_name='published_at', lookup_expr='gte')
    published_before = django_filters.DateTimeFilter(field_name='published_at', lookup_expr='lte')
    
    class Meta:
        model = Project
        fields = {
            'status': ['exact'],
            'title': ['icontains'],
            'description': ['icontains'],
        }