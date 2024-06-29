from django.urls import path
from custom_user.views import (
        Login,
        Registration,
        UserLogout,
        Notifications,
        Muted_or_Unmited,
        UserProfile,
        follow_or_unfollow, 
        change_profile_picture,
        ViewUserProfile)

urlpatterns=[
        path('login/',Login,name='login'),
        path('reg/',Registration, name='reg'),
        path('logout/',UserLogout,name='logout'),
        path('profile/',UserProfile,name='profile'),
        path('chang_profile_picture/', change_profile_picture, name='change_profile_picture'),
        path('user-profile/<str:user_name>/',ViewUserProfile,name='user_profile'),
        path('follow_or_unfollow/<int:user_id>/',follow_or_unfollow, name='follow_or_unfollow_user'),
        path('notification/',Notifications,name='notification'),
        path('muted_unmuted/<int:user_id>/',Muted_or_Unmited,name='muted_unmuted')
 ]