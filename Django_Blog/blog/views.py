from django.shortcuts import render
from .models import Post


def home(request):
    """Return Blog Home."""
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    """Return Blog About."""
    return render(request, 'blog/about.html', {'title': 'About'})
