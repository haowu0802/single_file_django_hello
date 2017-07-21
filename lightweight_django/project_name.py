"""
Demonstrate how to make a single file hello world web application using Django (commonly referred as heavy weighted framework)
    run it with:    python hello.py runserver
    to use it as template for new Django project:
"""
import os  # for env var
import sys  # for using manage.py functions with arguments
from django.conf import settings  # for Django settings, settings must be set before importing other components

"""
env dependent settings
"""
DEBUG = os.environ.get('DEBUG', 'on') == 'on'  # get debug flag from env, default on
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))  # get secret_key from env, default 32 b rand
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')  # allowing all

"""
the Django settings, typically in settings.py
"""
settings.configure(
    DEBUG=DEBUG,  # using debug mode
    SECRET_KEY=SECRET_KEY,  # env dependent
    ALLOWED_HOSTS=ALLOWED_HOSTS,  # env dep
    ROOT_URLCONF=__name__,  # point outing to the right place
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


"""
above this point needs to run before below
"""
from django.conf.urls import url  # for routing in controller
from django.http import HttpResponse  # for constructing response in views
from django.core.wsgi import get_wsgi_application  # wsgi application for prod server, usually in wsgi.py

application = get_wsgi_application()  # init wsgi app

"""
application
"""

"""
the view, typically in a view.py file, but that's not a requirement of Django
"""


def index(request):
    return HttpResponse('Hello World from a single file Django web app')

"""
the routing, typically in a urls.py file
"""
urlpatterns = (
    url(r'^$', index),
)

"""
entry point
"""
if __name__ == "__main__":
    # import the execution method to run the server
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

