from django.contrib import admin
from .models import BlogArticles

@admin.register(BlogArticles)
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish')
    list_filter = ('publish','author')
    search_fields = ('title','body')
    raw_id_fields = ('author',)  # 显示用户详细信息
    date_hierarchy = 'publish' # 提供一个日期分组筛选
    ordering = ['publish','author']

