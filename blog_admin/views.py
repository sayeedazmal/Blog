from django.shortcuts import render
from django.views.generic import TemplateView
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout, get_user_model

User = get_user_model()
class index(TemplateView):
  

    def get(self,request,*args, **kwargs):
        return render(request, 'deshboard/index.html')

    def post(self, request, *args, **kwargs):
        pass


def Customlogin(request):

    # if request.method=="POST":
    #     username    = request.POST.get('username')
    #     password    = request.POST.get('password')
    #     user        = authenticate(request, username=username, password=password)
      
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request, f' welcome {username} !!')
    #         return redirect('blog_admin:index')

    #     else:
    #         messages.warning(request, "please Try Again")
    return render(request, 'deshboard/login.html')

def Customlogout(request):
    logout(request)
    return redirect('blog_admin:login')
