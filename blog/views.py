from django.shortcuts import render

posts = [
    {
        'author': 'Gabrikel',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 02, 2021'
    },
    {
        'author': 'LyaBrezinski',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 03, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

