from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomManager(BaseUserManager):

    def create_user(self, email, user_name,  password, **extra_fields):
     
        extra_fields.setdefault('user_type','visitor')
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault('is_verify',True)
        
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **extra_fields)
        
       
        user.set_password(password)
        user.save(using=self._db)
       
        return user

    def create_superuser(self, email, user_name, password, **extra_fields):
      
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault('is_verify',True)
        extra_fields.setdefault('user_type','developer')

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Superuser must have is_active=True"))
        if extra_fields.get("is_verify") is not True:
            raise ValueError(_("Superuser must have is_verify=True"))
      
            
        return self.create_user(email,user_name,password,**extra_fields)


    
    # def create_user(self,username,email,password,**extra_fields):
        
    #     if not username:
    #         raise ValueError(_('username must be set'))
        
    #     if not email:
    #         raise ValueError(_('user must have an email address'))
        
    #     if not password:
    #         raise ValueError(_('password must be set'))
                             
        
    #     email = self.normalize_email(email)
    #     user = self.model(username=username, email=email, password=password, **extra_fields)
        
    #     user.set_password(password)
    #     user.save()
    #     return user
    # def create_superuser(self, username, email, password, **extra_fields):
            # extra_fields.setdefault('is_staff', True)
            # extra_fields.setdefault('is_active',True)
            # extra_fields.setdefault('is_superuser',True)

            # if extra_fields.get('is_staff') is not True:
            #     raise ValueError(_('Supperuser must have is_staff = true'))
            # if extra_fields.get('is_superuser') is not True:
            #     raise ValueError(_('Superuser must have is_superuser = true'))
            
            # return self.create_user(username,email,password,**extra_fields)


        

