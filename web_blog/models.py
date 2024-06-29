
from datetime import datetime
from django.db import models
from custom_user.models import CustomUser
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify 



class Category(models.Model):
    title            = models.CharField(max_length=50, null=True, unique=True)
    banner_img      = models.ImageField(upload_to='category/')
    slug            = models.SlugField(null=True,blank=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    update_date     = models.DateTimeField(auto_now=True)
   
    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class Tags(models.Model):
    title            = models.CharField(max_length=50, null=True)
    slug             = models.SlugField(null=True,blank=True)
    created_date     = models.DateTimeField(auto_now_add=True)
    update_date      = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class Post(models.Model):
    user                = models.ForeignKey(CustomUser,
                        on_delete=models.CASCADE,
                        related_name='user_blogs')
    category            = models.ForeignKey(Category,
                        on_delete=models.CASCADE, 
                        related_name='category_blogs',
                        null=True)
    tags                 = models.ManyToManyField(Tags,
                        related_name='tag_blogs',
                        blank=True)
    likes               = models.ManyToManyField(CustomUser,
                        related_name='user_likes',
                        blank=True)
    post_title          = models.CharField(max_length=200,
                        null=True)
    slug                = models.SlugField(null=True,max_length=255,blank=True)
    banner              = models.ImageField(upload_to='blog_banners',null=True)
    description         = RichTextField()
    created_date        = models.DateTimeField(auto_now_add=True)
    update_date         = models.DateTimeField(auto_now=True)

       
    class Meta:
        verbose_name_plural = 'Post'

    def __str__(self):
        return self.post_title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.post_title)
        super().save(*args,**kwargs)

class CommentsPost(models.Model):
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE,null=True, related_name="blog_comments")
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'PostComment'

    def __str__(self):
        return self.comment
    
class ReplyPost(models.Model):
    user = models.ForeignKey(CustomUser,null=True,on_delete = models.CASCADE)
    comments = models.ForeignKey(CommentsPost, null=True, related_name="comment_replies", on_delete=models.CASCADE)
    reply_comments = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ReplyPost'
  


   

   
