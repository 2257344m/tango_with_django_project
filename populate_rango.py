import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.model import Category, Page

def populate()
    # Creating lists of dictionaries, which will contain the pages we wish to
    # add to each category. We will also make a dictionary of dictionaries
    # to contain the categories.
