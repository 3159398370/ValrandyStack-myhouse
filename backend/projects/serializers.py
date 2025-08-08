from rest_framework import serializers
from .models import Category, Tag, Project, ProjectImage, ProjectVideo
from django.contrib.auth import get_user_model

User = get_user_model()

class UserBriefSerializer(serializers.ModelSerializer):
    """
    用户简要信息序列化器
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'avatar']

class CategorySerializer(serializers.ModelSerializer):
    """
    项目分类序列化器
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class TagSerializer(serializers.ModelSerializer):
    """
    项目标签序列化器
    """
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class ProjectImageSerializer(serializers.ModelSerializer):
    """
    项目图片序列化器
    """
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'caption', 'order']

class ProjectVideoSerializer(serializers.ModelSerializer):
    """
    项目视频序列化器
    """
    class Meta:
        model = ProjectVideo
        fields = ['id', 'title', 'video_url', 'thumbnail', 'order']

class ProjectListSerializer(serializers.ModelSerializer):
    """
    项目列表序列化器
    """
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    author = UserBriefSerializer(read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'description', 'featured_image',
            'category', 'tags', 'status', 'author', 'published_at',
            'start_date', 'end_date', 'github_url', 'demo_url', 'views_count'
        ]

class ProjectDetailSerializer(serializers.ModelSerializer):
    """
    项目详情序列化器
    """
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    author = UserBriefSerializer(read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)
    videos = ProjectVideoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'description', 'content', 'featured_image',
            'category', 'tags', 'status', 'author', 'created_at', 'updated_at',
            'published_at', 'start_date', 'end_date', 'github_url', 'demo_url',
            'views_count', 'images', 'videos'
        ]

class ProjectCreateUpdateSerializer(serializers.ModelSerializer):
    """
    项目创建和更新序列化器
    """
    class Meta:
        model = Project
        fields = [
            'title', 'slug', 'description', 'content', 'featured_image',
            'category', 'tags', 'status', 'published_at', 'start_date',
            'end_date', 'github_url', 'demo_url'
        ]
    
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        project = Project.objects.create(**validated_data)
        project.tags.set(tags)
        return project
    
    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if tags is not None:
            instance.tags.set(tags)
        
        return instance

class ProjectImageCreateSerializer(serializers.ModelSerializer):
    """
    项目图片创建序列化器
    """
    class Meta:
        model = ProjectImage
        fields = ['project', 'image', 'caption', 'order']

class ProjectVideoCreateSerializer(serializers.ModelSerializer):
    """
    项目视频创建序列化器
    """
    class Meta:
        model = ProjectVideo
        fields = ['project', 'title', 'video_url', 'thumbnail', 'order']