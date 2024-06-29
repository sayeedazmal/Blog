from web_blog.models import Category
from todo_api.serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser

class todo_model_viewset(viewsets.ModelViewSet):
  

    queryset = Category.objects.all()
    serializer_class = TodoSerializer

#===================================================================================#
# from web_blog.models import Category
# from todo_api.serializers import TodoSerializer
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


# class TodoList_creatview(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = TodoSerializer


# class TodoRetrive_Update_Destroy(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = TodoSerializer

# ==========================================================================
# class TodoList_creatview(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = TodoSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class TodoRetrive_Update_Destroy(GenericAPIView,RetrieveModelMixin,
#                                  UpdateModelMixin,DestroyModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = TodoSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


#=======================================================================#

# from django.shortcuts import render

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import permissions
# from web_blog.models import Category
# from .serializers import TodoSerializer

# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse


# class TodoListApiView(APIView):
   
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
#     def get(self, request, pk=None, *args, **kwargs):
#         id = pk
#         if id is not None:
#             category = Category.objects.get(id=id)
#             serializer = TodoSerializer(category)
#             return Response(serializer.data)
       
#         category = Category.objects.all()
#         serializer = TodoSerializer(category, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
        
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg: Successfully inserted"})
#         return Response(serializer.errors)
    
#     def put(self, request,pk=None, *args, **kwargs):
#         id = pk  
#         category = Category.objects.get(id=id)
#         serializer = TodoSerializer(category,data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg: Successfully Updated"})
#         return Response(serializer.errors)
    
#     def patch(self, request,pk=None, *args, **kwargs):
#         id = pk
#         category = Category.objects.get(id=id)
#         data = request.data
#         serializer = TodoSerializer(category,data=data,partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg: Successfully partial Updated"})
#         return Response(serializer.errors)
    
#     def delete(self, request,pk=None, *args, **kwargs):
#         id = pk
#         category = Category.objects.get(id=id)
#         category.delete()
       
#         return Response({"msg: Successfully Deleted"})
        




# # def todoList(request):
# #     # Complex Data
# #     category = Category.objects.all()

# #     # python Native Data
# #     serializer = TodoSerializer(category,many=True)

# #     # render Json
# #     json_data = JSONRenderer().render(serializer.data)

# #     return HttpResponse(json_data, content_type = 'application/json')


# # def todoById(request,pk):
# #     # Complex Data
# #     category = Category.objects.get(id=pk)

# #     # python Native Data
# #     serializer = TodoSerializer(category)

# #     # render Json
# #     json_data = JSONRenderer().render(serializer.data)

# #     return HttpResponse(json_data, content_type = 'application/json')

