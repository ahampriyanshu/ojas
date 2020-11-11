from django.contrib import admin
from .models import Post, Comment, Author
import string 
from django.utils.text import slugify 

admin.site.site_header = "OJAS Adminstration"
admin.site.site_title = "OJAS"
admin.site.index_title = "Home"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'joined')
    date_hierarchy = 'joined'
    ordering = ['joined']
admin.site.register(Author, AuthorAdmin)


# class UrlHitAdmin(admin.ModelAdmin):
#     list_display = ('url', 'hits')
# admin.site.register(UrlHit, UrlHitAdmin)


# class HitCountAdmin(admin.ModelAdmin):
#     list_display = ('url_hit', 'ip', 'session', 'date')
#     date_hierarchy = 'date'
#     ordering = ['date']
# admin.site.register(HitCount, HitCountAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': (slugify('title'),)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(Post, PostAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)