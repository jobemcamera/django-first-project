from django.shortcuts import render

# Create your views here.

context = {'text': 'Estamos na Home', 'title': 'Home'}


def home(request):
    return render(
        request,
        'home/index.html',
        context
    )
