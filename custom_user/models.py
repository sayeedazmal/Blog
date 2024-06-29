from django.db import models
from datetime import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from custom_user.manager import CustomManager

# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
        USER_TYPE=(
            ('visitor','visitor'),
            ('developer','developer')
        )
        email           = models.EmailField(unique=True,null=True)
        user_name       = models.CharField(max_length=30, unique=True,null=True)
        first_name      = models.CharField(max_length=30,null=True)
        last_name       = models.CharField(max_length=30,null=True)
        profile_image   = models.ImageField(null=True, blank=True, upload_to="profile_images")
        followers       = models.ManyToManyField("Follow") # user er model er niche hoyate Follow Model name String hisebe ache
        USERNAME_FIELD  = 'email'
        REQUIRED_FIELDS = ['user_name']
        
        user_type       = models.CharField(max_length=50,choices=USER_TYPE, default=USER_TYPE[0])
        is_staff        = models.BooleanField(default=False)
        is_active       = models.BooleanField(default=False)
        is_superuser    = models.BooleanField(default=False)
        is_verify       = models.BooleanField(default=False)

        objects         = CustomManager()
        def __str__(self):
            return self.email
    
    
        def get_profile_image(self):
                url=""
                try:
                    url = self.profile_image.url
                except:
                    url = ""
                return url

class Follow(models.Model):
      followed = models.ForeignKey(CustomUser,related_name='user_followers',on_delete=models.CASCADE)
      followed_by = models.ForeignKey(CustomUser,related_name='user_follows', on_delete=models.CASCADE)     
      muted = models.BooleanField(default=False)
      created_date = models.DateTimeField(auto_now_add=True)

      def __str__(self)->str:
            return f"{self.followed_by.user_name} started following {self.followed.user_name}"