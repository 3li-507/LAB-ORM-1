from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Post

# Create your views here.

 
def home_view(request:HttpRequest):
    post=Post.objects.all()
    return render(request, 'main/index.html', {'posts': post})

 
# def add_post_view(request:HttpRequest):
#     if request.method == "POST":
#         print(request.POST)
#         new_post = Post(title=request.POST["title"], content=request.POST["content"],poster=request.FILES["poster"])
#         new_post.save()
#         return redirect('main:home_view')
def add_post_view(request: HttpRequest):
    if request.method == "POST":
        new_post = Post(
            title=request.POST["title"],
            content=request.POST["content"],
        )
        if request.FILES.get("poster"):
            new_post.poster = request.FILES["poster"]
        new_post.save()
        return redirect('main:home_view')
    return render(request, "main/add_post.html")
    
    return render(request, "main/add_post.html")

def detail_post_view(request:HttpRequest, poster_id:int):
    post = Post.objects.get(pk=poster_id)
    # print(post.title)

    return render(request, 'main/detail_post.html', {'post':post})

def update_post_view(request: HttpRequest, poster_id: int):
    post = Post.objects.get(pk=poster_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        # if request.FILES.get("poster"):
        #     post.poster = request.FILES["poster"]
        if 'poster' in request.FILES: post.poster= request.FILES["poster"]
        post.save()
        return redirect('main:detail_post_view', poster_id=post.pk)
    return render(request, 'main/update_post.html', {'post': post})


def delete_post_view(request: HttpRequest, poster_id: int):   # أضف
    post = Post.objects.get(pk=poster_id)
    post.delete()

    return redirect('main:home_view')
