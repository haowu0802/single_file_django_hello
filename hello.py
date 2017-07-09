"""
Demonstrate how to make a single file hello world web application using Django (commonly referred as heavy weighted framework)
    run it with:    python hello.py runserver
"""
# for manage
import sys  # for using manage.py with arguments

# for settings, settings must be set before importing other components
from django.conf import settings  # for Django settings

# the settings, typically in settings.py
settings.configure(
    DEBUG=True,  # using debug mode
    SECRET_KEY='somekeyhere',
    ROOT_URLCONF=__name__,  # point outing to the right place
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


# for controller
from django.conf.urls import url  # for routing
# for views
from django.http import HttpResponse  # for constructing response


# the view, typically in a view.py file, but that's not a requirement of Django
def index(request):
    return HttpResponse('Hello World from a single file Django web app')


# the routing, typically in a urls.py file
urlpatterns = (
    url(r'^$', index),
)


# runserver
if __name__ == "__main__":
    # import the execution method to run the server
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

