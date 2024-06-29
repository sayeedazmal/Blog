from email.charset import QP
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage,PageNotAnInteger
from django.core.paginator import Paginator
from .models import Category, Post, Tags,CommentsPost,ReplyPost
from django.db.models import Q
from .forms import BlogForm, TextForm
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from custom_user.models import CustomUser
from django.utils.text import slugify


#index section
def Home(request):
    posts = Post.objects.order_by('-created_date')
    context = {
        "blogs":posts,
    }
    return render(request, 'home.html',context)

def Blog(request):

    query_set = Post.objects.all().order_by('-created_date') 
    page = request.GET.get("page",1)
    paginator = Paginator(query_set, 5)  # Show 2 contacts per page.
   
    try:
       blogs = paginator.page(page)
      
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger: 
        blogs = paginator.page(1)
   

    context = {
        "blogs" :blogs,
        "paginator":paginator,
        "blog":query_set, 
    }

    return render(request, 'blog.html',context)
    
def Category_blog(request, slug):
    category = get_object_or_404(Category, slug = slug)
    query_set = category.category_blogs.all()
    tags = Tags.objects.order_by("-created_date")[:5]

    
    page = request.GET.get("page",1)
    paginator = Paginator(query_set, 1)  # Show 2 contacts per page.
   
    try:
       blogs = paginator.page(page)
      
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger: 
        blogs = paginator.page(1)
   


    context = {
        'blogs':blogs,
        'tags':tags,
        'category': category,
    }
    return render(request,'category_blog.html',context)
    
def Tags_blog(request, slug):
    tag_blog = get_object_or_404(Tags, slug = slug)
    query_set = tag_blog.tag_blogs.all()
    tags = Tags.objects.order_by("-created_date")[:5]
    
    page = request.GET.get("page",1)
    paginator = Paginator(query_set, 1)  # Show 2 contacts per page.
   
    try:
       blogs = paginator.page(page)
      
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger: 
        blogs = paginator.page(1)

    context = {
       
        'blogs':blogs,
        'tags': tags,
    }
    return render(request,'tags_blog.html',context)

def searchBlog(request):
    query = request.GET.get('search-blog')
    if query:
        posts = Post.objects.filter(Q(post_title__icontains=query)) 
    else:
        # If not searched, return default posts
        posts = Post.objects.all().order_by("-date_created")
    context={
        "blog":posts,
    }
    return render(request,'home.html',context)

def post_details(request,slug):
    form = TextForm()
    blog = get_object_or_404(Post, slug=slug)
    liked_by = request.user in blog.likes.all()
  
    if request.method == "POST" and request.user.is_authenticated:
     
        form = TextForm(request.POST)
        if form.is_valid():
            CommentsPost.objects.create(
                user=request.user,
                blog = blog,
                comment = form.cleaned_data.get('comments')
            )
            return redirect('details',slug=slug)
    context = {
        "blog":blog,
        'form':form,
        'liked_by':liked_by,
    }
    return render(request, 'post-details.html',context)

@login_required(login_url="login")
def add_reply(request,blog_id,comment_id):
    blog = get_object_or_404(Post,id=blog_id)
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            comments = get_object_or_404(CommentsPost,id=comment_id)
            reply = form.cleaned_data.get("comments")
            ReplyPost.objects.create(
                user = request.user,
                comments = comments,
                reply_comments = reply
            )


           
    return redirect('details', slug=blog.slug)

@login_required(login_url='login')
def like_blog(request,pk):
    context = {}
    blog = get_object_or_404(Post, pk=pk)

    if request.user in blog.likes.all():
        blog.likes.remove(request.user)
        context['liked'] = False
        context['like_count'] = blog.likes.all().count()
    else:
        blog.likes.add(request.user)
        context['liked'] = True
        context['like_count'] = blog.likes.all().count()
    return JsonResponse(context,safe=False)

@login_required(login_url='login')
def MyBlog(request):
    query_set = request.user.user_blogs.all()
    page = request.GET.get("page",1)
    paginator = Paginator(query_set, 10)  # Show 2 contacts per page.
    delete = request.GET.get('delete', None)

    if delete:
        blog = get_object_or_404(Post,pk=delete)
        if request.user.pk != blog.user.pk:
            return redirect('home')
        blog.delete()
        messages.success(request,f'Successfully Deleted!!')
        return redirect('myblog')
    try:
       blogs = paginator.page(page)
      
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger: 
        blogs = paginator.page(1)
   

    context = {
        "blogs" :blogs,
        "paginator":paginator,
       
    }
  
    return render(request,'my-blog.html',context)

@login_required(login_url='login')
def AddBlog(request):
    
    form = BlogForm()
  
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
       
        if form.is_valid():
            tags = request.POST.get('tags').split(',')
            user = get_object_or_404(CustomUser, pk = request.user.pk)
            category = get_object_or_404(Category, pk = request.POST.get('category'))
            blog = form.save(commit=False)
            blog.user = user
            blog.category = category
            blog.save()
            for tag in tags:
                tag_input = Tags.objects.filter(
                    title__iexact = tag.strip(),
                    slug__iexact = tag.strip()
                )
                if tag_input.exists():
                    t = tag_input.first()
                    blog.tags.add(t)
                else:
                    new_tag = Tags.objects.create(
                        title = tag.strip(),
                        slug = slugify(tag.strip()),
                    )
                    blog.tags.add(new_tag)
            messages.success(request, f'registration successful !!')
            return redirect('details', slug = blog.slug)
        else:
            print(form.errors)

    context = {
        'form':form,
      
    }
    return render(request,'add-blog.html', context)


@login_required(login_url='login')
def UpdateBlog(request,slug):

    blog = get_object_or_404(Post,slug = slug)
    form = BlogForm(instance=blog)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        
        if form.is_valid():
            if request.user.pk != blog.user.pk:
                return redirect('home')
            tags = request.POST.get('tags').split(',')
            user = get_object_or_404(CustomUser, pk = request.user.pk)
            category = get_object_or_404(Category, pk = request.POST.get('category'))
            blog = form.save(commit=False)
            blog.user = user
            blog.category = category
            blog.save()
            for tag in tags:
                tag_input = Tags.objects.filter(
                    title__iexact = tag.strip(),
                    slug__iexact = tag.strip()
                )
                if tag_input.exists():
                    t = tag_input.first()
                    blog.tags.add(t)
                else:
                    new_tag = Tags.objects.create(
                        title = tag.strip(),
                        slug = slugify(tag.strip()),
                    )
                    blog.tags.add(new_tag)
            messages.success(request, f'Updated blog successful !!')
            return redirect('details', slug = blog.slug)
        else:
            print(form.errors)

    context = {
        'form':form,
        'blog':blog
    }
    return render(request,'update-blog.html', context)

