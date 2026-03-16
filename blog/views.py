from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('title')
    return render(request, 'blog/post_list.html', {'posts': posts})

def resume(request):
    return render(request, 'blog/resume.html')


def test_zone(request):
    return render(request, 'blog/test_zone.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

