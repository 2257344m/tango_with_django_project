from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Rango says hey there partner! <a href="/rango/about/">About Page</a>')

def about(request):
    return HttpResponse('Rango says this is the about page. <a href="/rango/">Back</a>.')
