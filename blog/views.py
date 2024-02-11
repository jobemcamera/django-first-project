from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return HttpResponse('Blog')
  
def exemplo(request):
    return HttpResponse('Exemplo do blog')