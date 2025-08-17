from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# API文档配置
schema_view = get_schema_view(
    openapi.Info(
        title="ValrandyStack个人网站API",
        default_version='v1',
        description="ValrandyStack个人网站的RESTful API文档",
        terms_of_service="https://www.valrandystack.com/terms/",
        contact=openapi.Contact(email="contact@valrandystack.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def home_view(request):
    """首页视图，显示API信息"""
    html_content = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ValrandyStack 个人网站 API</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                margin: 0;
                padding: 40px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container {
                text-align: center;
                max-width: 600px;
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 2.5em;
                margin-bottom: 20px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
            p {
                font-size: 1.2em;
                margin-bottom: 30px;
                opacity: 0.9;
            }
            .links {
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
            }
            .link {
                display: inline-block;
                padding: 12px 24px;
                background: rgba(255, 255, 255, 0.2);
                color: white;
                text-decoration: none;
                border-radius: 10px;
                transition: all 0.3s ease;
                border: 1px solid rgba(255, 255, 255, 0.3);
            }
            .link:hover {
                background: rgba(255, 255, 255, 0.3);
                transform: translateY(-2px);
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
            }
            .status {
                margin-top: 30px;
                padding: 15px;
                background: rgba(0, 255, 0, 0.2);
                border-radius: 10px;
                border: 1px solid rgba(0, 255, 0, 0.3);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 ValrandyStack API</h1>
            <p>欢迎使用 ValrandyStack 个人网站后端 API 服务</p>
            
            <div class="links">
                <a href="/swagger/" class="link">📚 API 文档 (Swagger)</a>
                <a href="/redoc/" class="link">📖 API 文档 (ReDoc)</a>
                <a href="/admin/" class="link">⚙️ 管理后台</a>
            </div>
            
            <div class="status">
                <strong>✅ 服务状态：正常运行</strong><br>
                Django 后端服务已成功启动
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    # 首页
    path('', home_view, name='home'),
    
    # 管理后台
    path('admin/', admin.site.urls),
    
    # API文档
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # API端点
    path('api/v1/users/', include('users.urls')),
    path('api/v1/projects/', include('projects.urls')),
    path('api/v1/creative_lab/', include('creative_lab.urls')),
    
    # 兼容性API端点（不带版本号）
    path('api/users/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/creative_lab/', include('creative_lab.urls')),
    
    # 认证
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]

# 在开发环境中提供媒体文件
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)