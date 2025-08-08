from django.db import models
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    """
    联系表单模型
    """
    STATUS_CHOICES = (
        ('new', _('新消息')),
        ('in_progress', _('处理中')),
        ('completed', _('已完成')),
        ('spam', _('垃圾邮件')),
    )
    
    name = models.CharField(_('姓名'), max_length=100)
    email = models.EmailField(_('邮箱'))
    phone = models.CharField(_('电话'), max_length=20, blank=True)
    subject = models.CharField(_('主题'), max_length=200)
    message = models.TextField(_('消息内容'))
    status = models.CharField(_('状态'), max_length=20, choices=STATUS_CHOICES, default='new')
    ip_address = models.GenericIPAddressField(_('IP地址'), blank=True, null=True)
    user_agent = models.TextField(_('用户代理'), blank=True)
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)
    admin_notes = models.TextField(_('管理员备注'), blank=True)
    
    class Meta:
        verbose_name = _('联系表单')
        verbose_name_plural = _('联系表单')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"