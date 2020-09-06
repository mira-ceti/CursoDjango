from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

def home(request):
    #return HttpResponse("Bienvenido a mi Blog")
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts': posts})

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {'post': post})
