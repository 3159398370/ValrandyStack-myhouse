from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    自定义用户模型，扩展Django默认的User模型
    """
    avatar = models.ImageField(_('头像'), upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(_('个人简介'), blank=True)
    website = models.URLField(_('个人网站'), blank=True)
    phone = models.CharField(_('电话'), max_length=20, blank=True)
    position = models.CharField(_('职位'), max_length=100, blank=True)
    company = models.CharField(_('公司'), max_length=100, blank=True)
    location = models.CharField(_('所在地'), max_length=100, blank=True)
    birth_date = models.DateField(_('出生日期'), null=True, blank=True)
    github_username = models.CharField(_('GitHub用户名'), max_length=100, blank=True)
    twitter_username = models.CharField(_('Twitter用户名'), max_length=100, blank=True)
    linkedin_username = models.CharField(_('LinkedIn用户名'), max_length=100, blank=True)
    weibo_username = models.CharField(_('微博用户名'), max_length=100, blank=True)
    bilibili_username = models.CharField(_('哔哩哔哩用户名'), max_length=100, blank=True)
    
    class Meta:
        verbose_name = _('用户')
        verbose_name_plural = _('用户')
    
    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username