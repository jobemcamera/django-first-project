from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404

# Create your views here.


def blog(request):
    context = {
        'title': 'Blog',
        'text': 'Estamos no Blog',
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')
    

    context = {
        'title': 'Post ' + str(found_post['id']),
        'text': 'Post ' + str(found_post['id']),
        'post': found_post
    }

    return render(request, 'blog/post.html', context)
