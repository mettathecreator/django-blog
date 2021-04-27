from django.contrib import admin
from  .models import Post, Comment


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'post', 'created_on')
    list_filter = ('created_on')
    search_fields = ('email', 'body')