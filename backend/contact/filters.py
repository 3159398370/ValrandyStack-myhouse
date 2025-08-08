import django_filters
from .models import Contact

class ContactFilter(django_filters.FilterSet):
    """
    联系表单过滤器
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    subject = django_filters.CharFilter(lookup_expr='icontains')
    message = django_filters.CharFilter(lookup_expr='icontains')
    created_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    
    class Meta:
        model = Contact
        fields = {
            'status': ['exact'],
        }