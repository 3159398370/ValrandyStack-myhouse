from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    自定义权限，只允许对象的作者编辑它
    """
    
    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求
        # 所以我们总是允许GET, HEAD 或 OPTIONS 请求
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 写入权限只允许对象的作者
        return obj.author == request.user or request.user.is_staff