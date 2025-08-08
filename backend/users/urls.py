from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# 创建路由器并注册视图集
router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]