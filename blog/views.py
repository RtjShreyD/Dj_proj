from django.shortcuts import render

posts = [
    {
        'author': 'Shreyansh',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 2, 2019'
    },
    {
        'author': 'Rtj',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 2, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
