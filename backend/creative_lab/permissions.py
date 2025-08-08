from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    自定义权限，允许任何人读取，但只有作者可以编辑
    """
    
    def has_permission(self, request, view):
        # 允许所有人进行安全的方法（GET, HEAD, OPTIONS）
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 写入权限只允许已认证的用户
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # 允许所有人进行安全的方法（GET, HEAD, OPTIONS）
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 写入权限只允许作者或管理员
        return obj.author == request.user or request.user.is_staff