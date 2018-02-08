"""Rango app URL Configuration
"""

from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$',
        views.index, name='index'),
    url(r'^about/',
        views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^polls-overview/',
        views.polls, name='polls-overview'),
    url(r'^polls/(?P<question_id>[0-9]+)/$',
        views.detail, name='detail'),
    url(r'^polls/(?P<question_id>[0-9]+)/results/$',
        views.results, name='results'),
    url(r'^polls/(?P<question_id>[0-9]+)/vote/$',
        views.vote, name='vote'),
]
