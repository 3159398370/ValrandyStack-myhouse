from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer, UserCreateSerializer,
    UserUpdateSerializer, PasswordChangeSerializer
)

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    用户视图集，提供用户的CRUD操作
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        # 注册用户时不需要认证
        if self.action == 'create':
            return [permissions.AllowAny()]
        # 用户详情可以被任何人查看
        elif self.action in ['retrieve', 'list']:
            return [permissions.IsAuthenticatedOrReadOnly()]
        # 其他操作需要认证
        return [permissions.IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return UserSerializer
    
    def get_queryset(self):
        # 普通用户只能查看自己的信息
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.id)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """
        获取当前登录用户的信息
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], serializer_class=PasswordChangeSerializer)
    def change_password(self, request):
        """
        修改密码
        """
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "密码修改成功"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)