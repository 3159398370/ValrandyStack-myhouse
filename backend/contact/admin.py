from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'ip_address', 'user_agent', 'created_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        (_('联系人信息'), {
            'fields': ('name', 'email', 'phone')
        }),
        (_('消息内容'), {
            'fields': ('subject', 'message')
        }),
        (_('状态信息'), {
            'fields': ('status', 'admin_notes')
        }),
        (_('技术信息'), {
            'fields': ('ip_address', 'user_agent', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_completed', 'mark_as_in_progress', 'mark_as_spam']
    
    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = _('标记为已完成')
    
    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
    mark_as_in_progress.short_description = _('标记为处理中')
    
    def mark_as_spam(self, request, queryset):
        queryset.update(status='spam')
    mark_as_spam.short_description = _('标记为垃圾邮件')
    
    def has_add_permission(self, request):
        # 禁止管理员手动添加联系表单
        return False