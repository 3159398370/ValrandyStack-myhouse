from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    用户序列化器，用于展示用户信息
    """
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'avatar',
            'bio', 'website', 'position', 'company', 'location',
            'github_username', 'twitter_username', 'linkedin_username',
            'weibo_username', 'bilibili_username', 'date_joined', 'last_login'
        ]
        read_only_fields = ['id', 'date_joined', 'last_login']

class UserCreateSerializer(serializers.ModelSerializer):
    """
    用户创建序列化器，用于注册新用户
    """
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'password_confirm',
            'first_name', 'last_name'
        ]
    
    def validate(self, attrs):
        # 验证两次密码输入是否一致
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "两次密码输入不一致"})
        
        # 验证密码强度
        try:
            validate_password(attrs['password'])
        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        
        return attrs
    
    def create(self, validated_data):
        # 移除password_confirm字段
        validated_data.pop('password_confirm', None)
        
        # 创建用户
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    """
    用户更新序列化器，用于更新用户信息
    """
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'avatar', 'bio', 'website',
            'phone', 'position', 'company', 'location', 'birth_date',
            'github_username', 'twitter_username', 'linkedin_username',
            'weibo_username', 'bilibili_username'
        ]

class PasswordChangeSerializer(serializers.Serializer):
    """
    密码修改序列化器
    """
    old_password = serializers.CharField(required=True, style={'input_type': 'password'})
    new_password = serializers.CharField(required=True, style={'input_type': 'password'})
    new_password_confirm = serializers.CharField(required=True, style={'input_type': 'password'})
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("旧密码不正确")
        return value
    
    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({"new_password": "两次新密码输入不一致"})
        
        try:
            validate_password(attrs['new_password'])
        except ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})
        
        return attrs