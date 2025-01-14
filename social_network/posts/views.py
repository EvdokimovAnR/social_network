from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostAdd


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


