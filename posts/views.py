# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Forms
    # Posts
from posts.forms import PostForm

# Models
    #Posts
from posts.models import Post


@login_required
def list_posts(request):
    posts: Post = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )