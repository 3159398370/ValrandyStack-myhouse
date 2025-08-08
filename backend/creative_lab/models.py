from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone

class Tag(models.Model):
    """
    创意实验室标签模型
    """
    name = models.CharField(_('名称'), max_length=50)
    slug = models.SlugField(_('别名'), max_length=50, unique=True)
    
    class Meta:
        verbose_name = _('实验室标签')
        verbose_name_plural = _('实验室标签')
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    """
    创意作品模型
    """
    STATUS_CHOICES = (
        ('draft', _('草稿')),
        ('published', _('已发布')),
        ('archived', _('已归档')),
    )
    
    title = models.CharField(_('标题'), max_length=200)
    slug = models.SlugField(_('别名'), max_length=200, unique=True)
    excerpt = models.TextField(_('摘要'), blank=True)
    content = models.TextField(_('内容'))
    featured_image = models.ImageField(_('特色图片'), upload_to='creative_lab/featured/', blank=True, null=True)
    status = models.CharField(_('状态'), max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creative_posts', verbose_name=_('作者'))
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True, verbose_name=_('标签'))
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)
    published_at = models.DateTimeField(_('发布时间'), null=True, blank=True)
    views_count = models.PositiveIntegerField(_('浏览次数'), default=0)
    likes_count = models.PositiveIntegerField(_('点赞次数'), default=0)
    comments_count = models.PositiveIntegerField(_('评论次数'), default=0)
    reading_time = models.PositiveIntegerField(_('阅读时间(分钟)'), default=0)
    
    class Meta:
        verbose_name = _('创意作品')
        verbose_name_plural = _('创意作品')
        ordering = ['-published_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # 计算阅读时间（假设平均阅读速度为每分钟200个单词）
        if self.content:
            word_count = len(self.content.split())
            self.reading_time = max(1, round(word_count / 200))
        
        super().save(*args, **kwargs)

class Comment(models.Model):
    """
    评论模型
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name=_('作品'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creative_comments', verbose_name=_('作者'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name=_('父评论'))
    content = models.TextField(_('内容'))
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)
    is_approved = models.BooleanField(_('是否批准'), default=True)
    
    class Meta:
        verbose_name = _('评论')
        verbose_name_plural = _('评论')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.author.username}对{self.post.title}的评论"

class Like(models.Model):
    """
    点赞模型
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', verbose_name=_('作品'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creative_likes', verbose_name=_('用户'))
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('点赞')
        verbose_name_plural = _('点赞')
        unique_together = ('post', 'user')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username}点赞了{self.post.title}"