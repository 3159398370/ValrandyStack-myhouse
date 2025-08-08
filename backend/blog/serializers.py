from rest_framework import serializers
from .models import Tag, Post, Comment, Like
from django.contrib.auth import get_user_model

User = get_user_model()

class UserBriefSerializer(serializers.ModelSerializer):
    """
    用户简要信息序列化器
    """
    full_name = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'avatar']

class TagSerializer(serializers.ModelSerializer):
    """
    博客标签序列化器
    """
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class CommentSerializer(serializers.ModelSerializer):
    """
    评论序列化器
    """
    author = UserBriefSerializer(read_only=True)
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'parent', 'content', 'created_at', 'updated_at', 'is_approved', 'replies']
        read_only_fields = ['is_approved']
    
    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.filter(is_approved=True), many=True).data
        return []

class CommentCreateSerializer(serializers.ModelSerializer):
    """
    评论创建序列化器
    """
    class Meta:
        model = Comment
        fields = ['post', 'parent', 'content']

class LikeSerializer(serializers.ModelSerializer):
    """
    点赞序列化器
    """
    user = UserBriefSerializer(read_only=True)
    
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']

class PostListSerializer(serializers.ModelSerializer):
    """
    博客文章列表序列化器
    """
    author = UserBriefSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt', 'featured_image',
            'author', 'tags', 'published_at', 'views_count',
            'likes_count', 'comments_count', 'reading_time'
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    """
    博客文章详情序列化器
    """
    author = UserBriefSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt', 'content', 'featured_image',
            'status', 'author', 'tags', 'created_at', 'updated_at',
            'published_at', 'views_count', 'likes_count', 'comments_count',
            'reading_time', 'comments', 'is_liked'
        ]
    
    def get_comments(self, obj):
        # 只返回顶级评论（没有父评论的评论）
        comments = obj.comments.filter(parent=None, is_approved=True)
        return CommentSerializer(comments, many=True).data
    
    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    """
    博客文章创建和更新序列化器
    """
    class Meta:
        model = Post
        fields = [
            'title', 'slug', 'excerpt', 'content', 'featured_image',
            'status', 'tags', 'published_at'
        ]
    
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        post.tags.set(tags)
        return post
    
    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if tags is not None:
            instance.tags.set(tags)
        
        return instance