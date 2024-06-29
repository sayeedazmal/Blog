from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin
from .models import CustomUser,Follow

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['user_name','user_type'] 

@admin.register(Follow)
class Follow(admin.ModelAdmin):
    list_display = ['followed','followed_by','muted','created_date']  