from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.conf import settings

class Category(models.Model):
    """
    项目分类模型
    """
    name = models.CharField(_('名称'), max_length=100)
    slug = models.SlugField(_('别名'), max_length=100, unique=True)
    description = models.TextField(_('描述'), blank=True)
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)
    
    class Meta:
        verbose_name = _('项目分类')
        verbose_name_plural = _('项目分类')
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Tag(models.Model):
    """
    项目标签模型
    """
    name = models.CharField(_('名称'), max_length=50)
    slug = models.SlugField(_('别名'), max_length=50, unique=True)
    
    class Meta:
        verbose_name = _('项目标签')
        verbose_name_plural = _('项目标签')
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Project(models.Model):
    """
    项目模型
    """
    STATUS_CHOICES = (
        ('draft', _('草稿')),
        ('published', _('已发布')),
        ('archived', _('已归档')),
    )
    
    title = models.CharField(_('标题'), max_length=200)
    slug = models.SlugField(_('别名'), max_length=200, unique=True)
    description = models.TextField(_('简短描述'))
    content = models.TextField(_('详细内容'))
    featured_image = models.ImageField(_('特色图片'), upload_to='projects/featured/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects', verbose_name=_('分类'))
    tags = models.ManyToManyField(Tag, related_name='projects', blank=True, verbose_name=_('标签'))
    status = models.CharField(_('状态'), max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects', verbose_name=_('作者'))
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)
    published_at = models.DateTimeField(_('发布时间'), null=True, blank=True)
    start_date = models.DateField(_('开始日期'), null=True, blank=True)
    end_date = models.DateField(_('结束日期'), null=True, blank=True)
    github_url = models.URLField(_('GitHub链接'), blank=True)
    demo_url = models.URLField(_('演示链接'), blank=True)
    views_count = models.PositiveIntegerField(_('浏览次数'), default=0)
    
    class Meta:
        verbose_name = _('项目')
        verbose_name_plural = _('项目')
        ordering = ['-published_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ProjectImage(models.Model):
    """
    项目图片模型
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name=_('项目'))
    image = models.ImageField(_('图片'), upload_to='projects/gallery/')
    caption = models.CharField(_('标题'), max_length=200, blank=True)
    order = models.PositiveIntegerField(_('排序'), default=0)
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('项目图片')
        verbose_name_plural = _('项目图片')
        ordering = ['order']
    
    def __str__(self):
        return f"{self.project.title} - 图片 {self.id}"

class ProjectVideo(models.Model):
    """
    项目视频模型
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='videos', verbose_name=_('项目'))
    title = models.CharField(_('标题'), max_length=200)
    video_url = models.URLField(_('视频链接'))
    thumbnail = models.ImageField(_('缩略图'), upload_to='projects/video_thumbnails/', blank=True, null=True)
    order = models.PositiveIntegerField(_('排序'), default=0)
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('项目视频')
        verbose_name_plural = _('项目视频')
        ordering = ['order']
    
    def __str__(self):
        return self.title