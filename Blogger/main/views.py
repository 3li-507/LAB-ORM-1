from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Post

# Create your views here.

 
def home_view(request:HttpRequest):
    post=Post.objects.all()
    return render(request, 'main/index.html', {'posts': post})

 
def add_post_view(request:HttpRequest):
    if request.method == "POST":
        print(request.POST)
        new_post = Post(title=request.POST["title"], content=request.POST["content"])
        new_post.save()
        return redirect('home_view')
    return render(request, "main/add_post.html")
