from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Aaron Glenn',
        'title': 'Blog 1',
        'content': 'My First Blog',
        'date_posted': 'January 1, 2020'
    },
    {
        'author': 'Aaron Glenn',
        'title': 'Blog 2',
        'content': 'My Second Blog',
        'date_posted': 'January 2, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
