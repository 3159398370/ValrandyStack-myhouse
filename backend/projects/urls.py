from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, TagViewSet, ProjectViewSet,
    ProjectImageViewSet, ProjectVideoViewSet
)

# 创建路由器并注册视图集
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'', ProjectViewSet)
router.register(r'images', ProjectImageViewSet)
router.register(r'videos', ProjectVideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]