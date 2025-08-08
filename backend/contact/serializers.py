from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    """
    联系表单序列化器
    """
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'subject', 'message', 'created_at']
        read_only_fields = ['created_at']
    
    def validate_email(self, value):
        """
        验证邮箱格式
        """
        if not value:
            raise serializers.ValidationError("邮箱地址不能为空")
        return value
    
    def validate_message(self, value):
        """
        验证消息内容
        """
        if len(value) < 10:
            raise serializers.ValidationError("消息内容太短，请详细描述您的问题或需求")
        return value

class ContactAdminSerializer(serializers.ModelSerializer):
    """
    管理员使用的联系表单序列化器
    """
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['name', 'email', 'phone', 'subject', 'message', 'ip_address', 'user_agent', 'created_at']