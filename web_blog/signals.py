from django.shortcuts import render
from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
# Create your views here.
from .models import Post
from custom_user.models import CustomUser, Follow
from notification.models import Notification


@receiver(post_save, sender=Post)
def send_notification_to_followers_when_blog_post(instance,created,*args,**kwargs):
    if created:
        followers = instance.user.followers.all()
        for data in followers:
            follower = data.followed_by
            if not data.muted:
                Notification.objects.create(
                    content_object = instance,
                    user = follower,
                    text = f"{instance.user.user_name} posted a new blog",
                    notification_type = "Post"
                )

@receiver(post_save, sender=Follow)
def send_notification_when_somone_followed(instance,created,*args,**kwargs):
    if created:
        followed = instance.followed
      
        if not instance.muted:
            Notification.objects.create(
                content_object = instance,
                user = followed,
                text = f"{instance.followed_by.user_name} started following you",
                notification_type = "Follow"
            )

@receiver(m2m_changed, sender=Post.likes.through)
def send_notification_to_somone_likes_blog_post(instance,pk_set, action, *args,**kwargs):
        pk = list(pk_set)[0]
        user = CustomUser.objects.get(pk=pk)
        if action  == 'post_add':
            Notification.objects.create(
                content_object = instance,
                user = instance.user,
                text = f"{user.user_name} likes your blog",
                notification_type = "Like"
            )