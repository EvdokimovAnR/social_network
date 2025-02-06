from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .models import Post, Comment
from .forms import PostAdd, CommentAdd


def index(request):
    if request.method == 'POST':
        form = PostAdd(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse('posts:index'))
    posts = Post.objects.all().order_by('-created_at')
    user = request.user
    posts_count = 0
    if request.user.is_authenticated:
        posts_count = Post.objects.filter(user=user).count()
    context = {'user': user, 'posts': posts, 'posts_count': posts_count}
    return render(request, 'posts/index.html', context)


def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    posts_count = 0
    if request.user.is_authenticated:
        posts_count = Post.objects.filter(user=request.user).count()
    context = {'posts':posts, 'posts_count': posts_count}
    return render(request, 'posts/index.html', context)


def user_posts(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    posts_count = 0
    if request.user.is_authenticated:
        posts_count = Post.objects.filter(user=request.user).count()
    context = {'posts': posts, 'posts_count': posts_count}
    return render(request, 'posts/index.html', context)


def comment_add(request):
    if request.method == 'POST':
        form = CommentAdd(data=request.POST)
        if form.is_valid():
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('posts:index'))
    else:
        form = CommentAdd()
    comments = Comment.objects.all()
    context = {'form': form, 'comments': comments}
    return render(request, 'posts/index.html', context)










