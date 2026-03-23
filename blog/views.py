from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
import markdown
import nh3

# Create your views here.
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('title')
    return render(request, 'blog/post_list.html', {'posts': posts})

def resume(request):
    return render(request, 'blog/resume.html')


def test_zone(request):
    return render(request, 'blog/test_zone.html')

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post':post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # No markdown conversion needed! 
    # Just send the clean HTML from the database to the template.
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()

            # --- UPDATED SANITIZATION STEP ---
            allowed_tags = {"h1", "h2", "h3", "p", "b", "i", "u", "ul", "ol", "li", "blockquote", "img", "a"}

            allowed_attributes = {
                "a": {"href", "title", "target"},  # Tell nh3 that <a> tags can keep these
                "img": {"src", "alt"},             # Tell nh3 that <img> tags can keep these
            }

            # Call nh3 to scrub the text
            post.text = nh3.clean(post.text, tags=allowed_tags, attributes=allowed_attributes)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()

            # --- UPDATED SANITIZATION STEP ---
            allowed_tags = {"h1", "h2", "h3", "p", "b", "i", "u", "ul", "ol", "li", "blockquote", "img", "a", "strong", "em"}

            allowed_attributes = {
                "a": {"href", "title", "target"},  # Tell nh3 that <a> tags can keep these
                "img": {"src", "alt", "width", "height", "style", "class"}, # Added more image control
            }

            # Call nh3 to scrub the text
            post.text = nh3.clean(post.text, tags=allowed_tags, attributes=allowed_attributes)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
# https://docs.djangoproject.com/en/5.1/topics/forms/

