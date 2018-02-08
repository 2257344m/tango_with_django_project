from django.shortcuts import render
from django.http import HttpResponse, Http404

from rango.models import Category, Page, Question

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    
    context_dict = {'categories': category_list,
                    'pages': page_list,
                    }


    return render(request, 'rango/index.html', context_dict)

def about(request):

    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:

        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)

def polls(request):
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   
    context_dict = {'latest_question_list': latest_question_list,
                   }
    
    return render(request, 'polls/index.html', context_dict)
        
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
