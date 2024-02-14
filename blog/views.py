from django.shortcuts import render

# Create your views here.

context = {'text': 'Estamos no Blog', 'title': 'Blog'}


def blog(request):
    return render(request, 'blog/index.html', context)


def exemplo(request):
    return render(request, 'blog/exemplo.html')
