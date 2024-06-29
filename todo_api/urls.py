# from todo_api import views
# from django.urls import path,include
# from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo_api import views

#create Router
router = DefaultRouter()
#Router register
router.register('todo',views.todo_model_viewset, basename='todo')

urlpatterns = [
    # path('todo',TodoListApiView.as_view()),
    # path('todo/<int:pk>',TodoListApiView.as_view()),

    # path('todo', TodoList_creatview.as_view()),
    # path('todo/<int:pk>/', TodoRetrive_Update_Destroy.as_view()),

    path('',include(router.urls)),
 
]