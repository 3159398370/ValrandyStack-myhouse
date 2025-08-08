from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact
from .serializers import ContactSerializer, ContactAdminSerializer
from .filters import ContactFilter

class ContactViewSet(viewsets.ModelViewSet):
    """
    联系表单视图集
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ContactFilter
    search_fields = ['name', 'email', 'subject', 'message']
    ordering_fields = ['created_at', 'status']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ContactAdminSerializer
        return ContactSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    
    def create(self, request, *args, **kwargs):
        # 获取客户端IP和用户代理
        ip_address = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        # 添加IP和用户代理到数据中
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        # 保存联系表单
        contact = serializer.save(
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        # 发送通知邮件给管理员
        self.send_notification_email(contact)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_client_ip(self, request):
        """
        获取客户端IP地址
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def send_notification_email(self, contact):
        """
        发送通知邮件给管理员
        """
        subject = f'新的联系表单消息: {contact.subject}'
        message = f"""收到新的联系表单消息：
        
姓名: {contact.name}
邮箱: {contact.email}
电话: {contact.phone}
主题: {contact.subject}
消息内容: 
{contact.message}

IP地址: {contact.ip_address}
提交时间: {contact.created_at}
"""
        
        # 检查是否配置了邮件设置
        if hasattr(settings, 'ADMIN_EMAIL') and settings.EMAIL_HOST:
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # 记录错误但不影响API响应
                print(f"发送通知邮件失败: {str(e)}")