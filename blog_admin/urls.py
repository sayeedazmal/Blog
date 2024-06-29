from django.urls import path
from blog_admin import views

app_name = 'blog_admin'

urlpatterns=[
        path('deshboard/admin', views.index.as_view(), name = 'index'),
        path('deshboard/login',views.Customlogin, name='login'),
        path('deshboard/logout', views.Customlogout, name='logout'),
      
 ]
