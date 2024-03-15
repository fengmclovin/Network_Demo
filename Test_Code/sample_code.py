# network/models.py

class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# network/views.py

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(user=request.user, content=content)
            return redirect('index')  # Assuming you have an 'index' view for the homepage
    return render(request, 'network/create_post.html')

@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post:
        Like.objects.create(user=request.user, post=post)
    return redirect('index')  # Redirect to the homepage after liking the post

# network/urls.py

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    # Other URL patterns...
]
