from django.contrib import admin
from web_blog.models import Category,Tags,Post,CommentsPost,ReplyPost


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['id','title','banner_img','slug','created_date','update_date']

@admin.register(Tags)
class Tags(admin.ModelAdmin):
    list_display = ['id','title','created_date','update_date']

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ['id','user','category','post_title','slug','banner','description',
                   'created_date','update_date']

@admin.register(CommentsPost)
class CommentsPost(admin.ModelAdmin):
    list_display = ['id','user','blog','comment','created_date','update_date']

@admin.register(ReplyPost)
class ReplyPost(admin.ModelAdmin):
    list_display = ['id','user','comments','reply_comments','created_date','update_date']

