#!/usr/bin/python
from __future__ import division
import os
import sys
import json

from django.conf import settings

DEBUG = os.environ.get('DEBUG','on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS','localhost').split(',')


settings.configure(
        DEBUG = DEBUG,
        SECRET_KEY = SECRET_KEY,
        ALLOWED_HOSTS = ALLOWED_HOSTS,
        ROOT_URLCONF = __name__,

        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ),
        )

from django.http import HttpResponse
from django.conf.urls import url, patterns
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

def index(request):
    return HttpResponse("Hello World")

def btcmxn(request):
    btc = 3000.59
    mxn = float("{0:.6f}".format(1/3000))
    quote = {"MXN":mxn,"BTC":btc}
    quote_json = json.dumps(quote)
    return HttpResponse(quote_json)

urlpatterns= patterns('',
        url(r'^$', index),
        url(r'^hello/$', btcmxn),
        
        )

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
