from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import Category, Tag, Project, ProjectImage, ProjectVideo
from .serializers import (
    CategorySerializer, TagSerializer,
    ProjectListSerializer, ProjectDetailSerializer, ProjectCreateUpdateSerializer,
    ProjectImageSerializer, ProjectImageCreateSerializer,
    ProjectVideoSerializer, ProjectVideoCreateSerializer
)
from .permissions import IsAuthorOrReadOnly
from .filters import ProjectFilter

class CategoryViewSet(viewsets.ModelViewSet):
    """
    项目分类视图集
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class TagViewSet(viewsets.ModelViewSet):
    """
    项目标签视图集
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class ProjectViewSet(viewsets.ModelViewSet):
    """
    项目视图集
    """
    queryset = Project.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProjectFilter
    search_fields = ['title', 'description', 'content']
    ordering_fields = ['published_at', 'created_at', 'views_count', 'title']
    lookup_field = 'slug'
    
    def get_queryset(self):
        # 非管理员用户只能看到已发布的项目
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Project.objects.all()
        elif self.request.user.is_authenticated:
            # 登录用户可以看到自己的草稿
            return Project.objects.filter(
                models.Q(status='published') | 
                models.Q(author=self.request.user)
            )
        # 匿名用户只能看到已发布的项目
        return Project.objects.filter(status='published')
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProjectCreateUpdateSerializer
        elif self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectListSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    @action(detail=True, methods=['post'])
    def increment_view(self, request, slug=None):
        """
        增加项目浏览次数
        """
        project = self.get_object()
        project.views_count += 1
        project.save()
        return Response({'status': 'view count incremented'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def related(self, request, slug=None):
        """
        获取相关项目
        """
        project = self.get_object()
        # 获取同一分类下的其他项目
        related_projects = Project.objects.filter(
            category=project.category,
            status='published'
        ).exclude(id=project.id)[:5]
        
        serializer = ProjectListSerializer(related_projects, many=True, context={'request': request})
        return Response(serializer.data)

class ProjectImageViewSet(viewsets.ModelViewSet):
    """
    项目图片视图集
    """
    queryset = ProjectImage.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProjectImageCreateSerializer
        return ProjectImageSerializer
    
    def get_queryset(self):
        # 过滤特定项目的图片
        project_slug = self.request.query_params.get('project', None)
        if project_slug is not None:
            return ProjectImage.objects.filter(project__slug=project_slug)
        return ProjectImage.objects.all()

class ProjectVideoViewSet(viewsets.ModelViewSet):
    """
    项目视频视图集
    """
    queryset = ProjectVideo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProjectVideoCreateSerializer
        return ProjectVideoSerializer
    
    def get_queryset(self):
        # 过滤特定项目的视频
        project_slug = self.request.query_params.get('project', None)
        if project_slug is not None:
            return ProjectVideo.objects.filter(project__slug=project_slug)
        return ProjectVideo.objects.all()