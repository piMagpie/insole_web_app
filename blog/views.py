from django.shortcuts import render


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Augost 27, 2018'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Augost 27, 2018'
    },
]

def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context) # request, template and context(arguments)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
