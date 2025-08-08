from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, PostViewSet, CommentViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet, basename='likes')

urlpatterns = [
    path('', include(router.urls)),
]