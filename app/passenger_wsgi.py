# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/МОЙUSER/data/www/МОЙСАЙТ.ru/project_name')
sys.path.insert(1, '/var/www/МОЙUSER/data/venv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()