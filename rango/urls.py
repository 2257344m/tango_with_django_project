"""Rango app URL Configuration
"""

from django.conf.urls import url
from rango import views

app_name = 'rango'
urlpatterns = [
    url(r'^$',
        views.index, name='index'),
    url(r'^about/',
        views.about, name='about'),
    url(r'add_category/$',
        views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        views.add_page, name='add_page'),
    url(r'^register/$',
        views.register, name='register'),
    url(r'^login/$',
        views.user_login, name='login'),
    url(r'^restricted/$',
        views.restricted, name='restricted'),
    url(r'^logout/$',
        views.user_logout, name='logout'),
    url(r'^polls/',
        views.PollsView.as_view(), name='polls'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$',
        views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',
        views.vote, name='vote'),
]
