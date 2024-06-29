from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login,logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Follow
from django.db.models import Q
from notification.models import Notification

# from Blog.custom_user.admin import CustomUser
from .forms import ProfilePictureUpdate, UserLoginFrom, UserUpdateProfile,UserRegistrationForm
# Create your views here.

# login section
def Login(request):
 
    form = UserLoginFrom()
    if request.method == 'POST':
        form = UserLoginFrom(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data.get('user_name'),
                password = form.cleaned_data.get('password')
                )
            print("USER is ", form.cleaned_data.get('username'))
            if user:
                login(request, user)
                
                return redirect('home')
            else:
                messages.warning(request,"wrong creadintial")
    context = {
        'form':form
    }
    return render(request,'login.html',context)

#Registration section
def Registration(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.set_password(form.cleaned_data.get('password'))
           user = CustomUser.objects.create_user(user_name=form.cleaned_data.get('user_name'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password'))
           user.save()
           messages.success(request, f'registration successful !!')
           return redirect('login')
         
    context = {
        "form": form
    }
    return render(request,'registration.html',context)

#logout section
def UserLogout(request):
    auth_logout(request)
    # messages.success(request, f' You Are in Logout !!')
    return redirect('login')

@login_required(login_url='login')
def UserProfile(request):
    account = get_object_or_404(CustomUser,pk=request.user.pk)
    form = UserUpdateProfile(instance=account)
    if request.method == "POST":
        if request.user.pk != account.pk:
            return redirect("home ")
        form = UserUpdateProfile(request.POST,instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been Updated Successfully ")
            return redirect('profile')
        else:
            print(form.errors)

    context = {
        "account":account,
        "form": form
    }
    return render(request, 'profile.html',context)

@login_required(login_url='login')
def change_profile_picture(request):
    if request.method == "POST":
        form = ProfilePictureUpdate(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['profile_picture']
            user = get_object_or_404(CustomUser,pk=request.user.pk)
            if request.user.pk != user.pk:
                return redirect('home')
            user.profile_image = image
            user.save()
            messages.success(request, "profile image Update successfully ")
        return redirect('profile')

@login_required(login_url='login')  
def ViewUserProfile(request,user_name):
    account_user = get_object_or_404(CustomUser, user_name=user_name)
    following = False
    muted = None
    if request.user.is_authenticated:
        if request.user.id == account_user.id:
            return redirect('profile') 
        followers = account_user.followers.filter(
            followed_by_id = request.user.id
            )
        if followers.exists():
            following = True

    if following:
        queryset = followers.first()
        if queryset.muted:
            muted=True
        else:
            muted = False

    context={
        'account_user':account_user,
        'following':following,
        'muted':muted 
        }
    return render(request,'view-user-profile.html',context)

@login_required(login_url='login')
def follow_or_unfollow(rquest, user_id):
   
    followed = get_object_or_404(CustomUser, id=user_id)
    followed_by = get_object_or_404(CustomUser, id = rquest.user.id)

    follow,create = Follow.objects.get_or_create(
        followed  = followed,
        followed_by  = followed_by
    )
    
    if create:
        followed.followers.add(follow)
    else:
        followed.followers.remove(follow)
        follow.delete()
    
    return redirect("user_profile", user_name = followed.user_name)

@login_required(login_url='login')
def Notifications(request):
    notifications = Notification.objects.filter(
        user = request.user,
        is_seen = False
    )
    for notification in notifications:
        notification.is_seen = True
        notification.save()

    return render(request, 'notification.html')

@login_required(login_url='login')
def Muted_or_Unmited(request,user_id):
    user = get_object_or_404(CustomUser,pk=user_id)
    follower = get_object_or_404(CustomUser,pk=request.user.pk)
  
    instance = get_object_or_404(
        Follow,
        followed = user,
        followed_by = follower
    )

    if instance.muted:
        instance.muted = False
        instance.save()
    else:
        instance.muted = True
        instance.save()
   
    return redirect('user_profile',user_name=user.user_name)