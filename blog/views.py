from django.shortcuts import render, get_object_or_404

#from django.shortcuts import render

# Create your views here.

#def index(request):
#    return render(request, "blog/index.html")
from django.utils import timezone
from blog.models import Post


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})

def post_detail_02(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post":post})

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})

def post_detail_01(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})
