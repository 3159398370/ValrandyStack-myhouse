from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Tag, Post, Comment, Like

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('author', 'content', 'is_approved', 'created_at')
    readonly_fields = ('author', 'created_at')
    can_delete = True
    show_change_link = True

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'published_at', 'views_count', 'likes_count', 'comments_count')
    list_filter = ('status', 'created_at', 'published_at', 'tags')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    filter_horizontal = ('tags',)
    inlines = [CommentInline]
    readonly_fields = ('views_count', 'likes_count', 'comments_count', 'reading_time')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'excerpt', 'content', 'featured_image')
        }),
        (_('发布信息'), {
            'fields': ('status', 'author', 'published_at', 'tags')
        }),
        (_('统计信息'), {
            'fields': ('views_count', 'likes_count', 'comments_count', 'reading_time'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # 如果是新建博客
            obj.author = request.user
        obj.save()

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'content_preview', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('content', 'author__username', 'post__title')
    raw_id_fields = ('post', 'author', 'parent')
    actions = ['approve_comments', 'disapprove_comments']
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = _('内容预览')
    
    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = _('批准选中的评论')
    
    def disapprove_comments(self, request, queryset):
        queryset.update(is_approved=False)
    disapprove_comments.short_description = _('取消批准选中的评论')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('post__title', 'user__username')
    raw_id_fields = ('post', 'user')