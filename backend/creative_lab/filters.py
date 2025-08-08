import django_filters
from django.db import models
from .models import Post

class PostFilter(django_filters.FilterSet):
    """
    创意作品过滤器
    """
    # 标题和内容模糊搜索
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    
    # 按标签过滤
    tag = django_filters.CharFilter(field_name='tags__slug')
    
    # 按作者过滤
    author = django_filters.CharFilter(field_name='author__username')
    
    # 按发布日期范围过滤
    published_after = django_filters.DateTimeFilter(field_name='published_at', lookup_expr='gte')
    published_before = django_filters.DateTimeFilter(field_name='published_at', lookup_expr='lte')
    
    # 按年月过滤
    year = django_filters.NumberFilter(field_name='published_at', lookup_expr='year')
    month = django_filters.NumberFilter(field_name='published_at', lookup_expr='month')
    
    class Meta:
        model = Post
        fields = {
            'status': ['exact'],
            'tags': ['exact'],
            'author': ['exact'],
        }