from django.contrib import admin
from .models import Post, Comment, Author

admin.site.site_header = "OJAS Adminstration"
admin.site.site_title = "OJAS"
admin.site.index_title = "Home"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'joined')
    date_hierarchy = 'joined'
    ordering = ['joined']
admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)