import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # Creating lists of dictionaries, which will contain the pages we wish to
    # add to each category. We will also make a dictionary of dictionaries
    # to contain the categories.

    # Page dictionaries

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 10},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views": 20},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         "views": 30}
        ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "http://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 40},
        {"title": "Django Rocks",
         "url": "https://www.djangorocks.com/",
         "views": 50},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 60}
        ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         "views": 70},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         "views": 80}
        ]

    # Category dictionary
    
    cats = {"Python": {"pages": python_pages,
                       "views": 128,
                       "likes": 64},
            "Django": {"pages": django_pages,
                       "views": 64,
                       "likes": 32},
            "Other Frameworks": {"pages": other_pages,
                                 "views": 32,
                                 "likes": 16}}

    # Iteration to use the dictionaries to create the pages/categories

    for cat, cat_data in cats.items():
            c = add_cat(cat, cat_data["views"], cat_data["likes"])
            for p in cat_data["pages"]:
                add_page(c, p["title"], p["url"], p["views"])

    # Printing those added categories

    for c in Category.objects.all():
            for p in Page.objects.filter(category=c):
                print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
            p = Page.objects.get_or_create(category=cat, title=title)[0]
            p.url=url
            p.views=views
            p.save()
            return p

def add_cat(name, views=0, likes=0):
            c = Category.objects.get_or_create(name=name)[0]
            c.views=views
            c.likes=likes
            c.save()
            return c

# Actual script execution

if __name__ == '__main__':
    print ("Starting Rango population script...")
    populate()
