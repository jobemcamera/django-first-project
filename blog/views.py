from django.shortcuts import render
from blog.data import posts

# Create your views here.

context = {
    'title': 'Blog',
    'text': 'Estamos no Blog',
    'posts': posts
}


def blog(request):
    return render(request, 'blog/index.html', context)


def exemplo(request):
    return render(request, 'blog/exemplo.html')
