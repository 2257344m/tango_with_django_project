from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # Creates a dictionary to pass the template engine as its context
    # Basically will make itself appear where 'boldmessage' is written in the html code
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Returns the rendered response to the client
    # The first parameter is the template we want to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse('Rango says this is the about page. <a href="/rango/">Back</a>.')
