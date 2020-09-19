from django.shortcuts import render

posts = [
    {
        'author': 'Starlight Romero',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 21, 2020'
    },
    {
        'author': 'Sid Arcidiacono',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 31, 2020'
    }
]


def home(request):
    """Return Blog Home."""
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    """Return Blog About."""
    return render(request, 'blog/about.html', {'title': 'About'})
