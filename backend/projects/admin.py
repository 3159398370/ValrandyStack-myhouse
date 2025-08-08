from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category, Tag, Project, ProjectImage, ProjectVideo

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'status', 'author', 'published_at', 'views_count')
    list_filter = ('status', 'category', 'tags', 'created_at', 'published_at')
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    filter_horizontal = ('tags',)
    inlines = [ProjectImageInline, ProjectVideoInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'content', 'featured_image')
        }),
        (_('分类与标签'), {
            'fields': ('category', 'tags')
        }),
        (_('发布信息'), {
            'fields': ('status', 'author', 'published_at')
        }),
        (_('项目信息'), {
            'fields': ('start_date', 'end_date', 'github_url', 'demo_url')
        }),
        (_('统计信息'), {
            'fields': ('views_count',),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # 如果是新建项目
            obj.author = request.user
        obj.save()

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'order', 'created_at')
    list_filter = ('project', 'created_at')
    search_fields = ('project__title', 'caption')

@admin.register(ProjectVideo)
class ProjectVideoAdmin(admin.ModelAdmin):
    list_display = ('project', 'title', 'order', 'created_at')
    list_filter = ('project', 'created_at')
    search_fields = ('project__title', 'title')