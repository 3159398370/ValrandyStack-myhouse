from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# API文档配置
schema_view = get_schema_view(
    openapi.Info(
        title="ValrandyStack API",
        default_version='v1',
        description="ValrandyStack个人网站API文档",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@valrandystack.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # 管理后台
    path('admin/', admin.site.urls),
    
    # API文档
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # REST框架认证
    path('api-auth/', include('rest_framework.urls')),
    
    # JWT认证
    path('api/token/', include('rest_framework_simplejwt.urls')),
    
    # 应用API
    path('api/users/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/creative_lab/', include('creative_lab.urls')),
    path('api/contact/', include('contact.urls')),
]

# 开发环境下提供媒体文件服务
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)