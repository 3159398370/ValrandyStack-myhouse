from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend

from .models import Tag, Post, Comment, Like
from .serializers import (
    TagSerializer, PostListSerializer, PostDetailSerializer,
    PostCreateUpdateSerializer, CommentSerializer, CommentCreateSerializer,
    LikeSerializer
)
from .permissions import IsAuthorOrReadOnly
from .filters import PostFilter

class TagViewSet(viewsets.ModelViewSet):
    """
    博客标签视图集
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'slug'
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()

class PostViewSet(viewsets.ModelViewSet):
    """
    博客文章视图集
    """
    queryset = Post.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'excerpt', 'content']
    ordering_fields = ['published_at', 'views_count', 'likes_count', 'comments_count']
    ordering = ['-published_at']
    
    def get_queryset(self):
        queryset = Post.objects.all()
        
        # 非管理员用户只能看到已发布的文章
        if not self.request.user.is_staff:
            queryset = queryset.filter(status='published')
        
        # 如果是作者，可以看到自己的所有文章
        if self.request.user.is_authenticated and not self.request.user.is_staff:
            queryset = Post.objects.filter(
                models.Q(status='published') | 
                models.Q(author=self.request.user)
            )
        
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return PostCreateUpdateSerializer
        return PostDetailSerializer
    
    def perform_create(self, serializer):
        # 设置作者为当前用户
        serializer.save(author=self.request.user)
        
        # 如果状态是已发布但没有设置发布时间，则设置为当前时间
        if serializer.validated_data.get('status') == 'published' and not serializer.validated_data.get('published_at'):
            serializer.save(published_at=timezone.now())
    
    def perform_update(self, serializer):
        # 如果状态从草稿变为已发布，且没有设置发布时间，则设置为当前时间
        instance = self.get_object()
        if instance.status != 'published' and serializer.validated_data.get('status') == 'published' and not instance.published_at:
            serializer.save(published_at=timezone.now())
        else:
            serializer.save()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # 增加浏览次数
        instance.views_count = F('views_count') + 1
        instance.save()
        instance.refresh_from_db()  # 刷新以获取更新后的值
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def like(self, request, slug=None):
        """
        点赞文章
        """
        post = self.get_object()
        user = request.user
        
        if not user.is_authenticated:
            return Response({"detail": "认证凭据未提供"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # 检查是否已经点赞
        like, created = Like.objects.get_or_create(post=post, user=user)
        
        if created:
            # 更新文章的点赞计数
            post.likes_count = F('likes_count') + 1
            post.save()
            post.refresh_from_db()
            return Response({"detail": "点赞成功", "likes_count": post.likes_count}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "已经点赞过该文章"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def unlike(self, request, slug=None):
        """
        取消点赞文章
        """
        post = self.get_object()
        user = request.user
        
        if not user.is_authenticated:
            return Response({"detail": "认证凭据未提供"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # 检查是否已经点赞
        try:
            like = Like.objects.get(post=post, user=user)
            like.delete()
            
            # 更新文章的点赞计数
            post.likes_count = F('likes_count') - 1
            post.save()
            post.refresh_from_db()
            return Response({"detail": "取消点赞成功", "likes_count": post.likes_count}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "未点赞该文章"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def related(self, request, slug=None):
        """
        获取相关文章
        """
        post = self.get_object()
        # 获取相同标签的文章，排除当前文章
        tags = post.tags.all()
        related_posts = Post.objects.filter(tags__in=tags, status='published').exclude(id=post.id).distinct()
        
        # 限制返回5篇相关文章
        related_posts = related_posts[:5]
        serializer = PostListSerializer(related_posts, many=True, context={'request': request})
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    """
    评论视图集
    """
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CommentCreateSerializer
        return CommentSerializer
    
    def perform_create(self, serializer):
        # 设置作者为当前用户
        comment = serializer.save(author=self.request.user)
        
        # 更新文章的评论计数
        post = comment.post
        post.comments_count = F('comments_count') + 1
        post.save()
    
    def perform_destroy(self, instance):
        # 更新文章的评论计数
        post = instance.post
        instance.delete()
        post.comments_count = F('comments_count') - 1
        post.save()

class LikeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    点赞视图集（只读）
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # 用户只能查看自己的点赞
        return Like.objects.filter(user=self.request.user)