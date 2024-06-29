from django.urls import path
from  web_blog.views import (Index,Blog,
                             Category_blog,
                             Tags_blog, 
                             searchBlog,
                             post_details,
                             add_reply,like_blog,
                             MyBlog,
                             AddBlog,
                             UpdateBlog,
                            
                             )
urlpatterns = [
    path('',Index, name='index'),

    path('blog/',Blog, name='blog'),
    path('cat_blog/<str:slug>/',Category_blog, name='cat_blog'),
    path('tag_blog/<str:slug>/', Tags_blog, name='tag_blog'),
    path('blog/post-details/<str:slug>/',post_details, name='details'),
    path('search/',searchBlog, name='search'),
    path('post/<int:blog_id>/<int:comment_id>',add_reply, name='reply'),
    path('like_blog/<int:pk>/',like_blog, name='like_blog'),

    path('myblog/', MyBlog, name='myblog'),
    path('addblog/', AddBlog, name='addblog'),
    path('updateblog/<str:slug>/',UpdateBlog, name='update'),
   
    

]
