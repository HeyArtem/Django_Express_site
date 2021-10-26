# Django_Express_site
В этом проекте, я создал простой проект и приложение в django и выложил его на свой хост.
(без базы данных, без миграций!)

что бы подключиться по ssh, в терминале ввожу:
ssh username@host
password:
в www хранится мой сайт
	или также можно в FileZilla

на локальной машине создаю свой проект
$ cd Desktop/ && ls
$  mkdir heyartem.ru && cd heyartem.ru && ls
$ python3 -m venv venv
$ source venv/bin/activate
$ sudo apt update
$ sudo apt upgrade -y
$ sudo apt autoremove
$ sudo apt autoclean
$ pip install -U pip
$ pip install -U django setuptools
$ django-admin startproject app
$ cd  app
$ django-admin startapp blog_app
$ cd ..
$ code .

Убедиться, что активировано вирт.окруж., и реги-ю приложение в settings 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog_app',
]

прописываю путь в главном urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls'))

]
в моем приложении создаю фаил urls.py, в нем импортирую путь из urls проекта и свою будущую функцию, приписываю путь
from django.urls import path
from .views import main_page

urlpatterns =[
    path('', main_page)
]

во views.py создаю представление (функцию main_page), прикрепляю к html странице
from django.shortcuts import render

def main_page(request):
    
    name = 'Max'
    name_2 = 'Artem'
    context = {
        'name': name,
        'name_2': name_2
    }
    
    return render(request, 'blog_app/blog_app_index.html', context=context)

в settings.py прописываю templates (импортирую os)
import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,

на одном уровне с приложением создаю директорию templates
в директрории templates создаю директорию blog_app
в директории templates создаю base.html
в директории blog_app создаю blog_app_index.html










                                      
заполняю base.html ( block content, title)
shift + ! = заполнит html, head, meta …
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>base</title>
</head>
<body>
    {% block content%}
    {% endblock %}
</body>
</html>

заполняю blog_app_index.html (вывожу context из функции во views.py)
{% extends 'base.html' %}

{% block content %}
    <h1>Этот проет создали {{name}} и {{name_2}}</h1>
{% endblock %}

в терминале vs code убедиться, что я в директории ~/Desktop/heyartem.ru/app и делаю контрольный запуск сервера
$ ./manage.py runserver
остановить сервер

в settings в  ALLOWED_HOSTS прописываю имя своего имя своего хоста, дописываю STATIC_URL 
ALLOWED_HOSTS = ['heyartem.ru', 'www.heyartem.ru']

STATIC_URL = '/static/'
STATIC_ROOT='static/'

создам директрию collectstatic в которую собираю статику со всего проекта (команда в терминале)
$ ./manage.py collectstatic

создам фаил passenger_wsgi.py на одном уровне с manage.py, вставляю в него код (с https://help.reg.ru/hc/ru/articles/4408047456785/ )

вставлю свою user, своё имя сайта и путь до интерпритатора, Исправлю версию python, исправить имя своего проекта
!!! в версии на Git этого нет!!!
# -*- coding: utf-8 -*- 
import os, sys 
sys.path.insert(0, '/var/www/МОЙUSER/data/www/heyartem.ru/project_name') 
sys.path.insert(1, '/var/www/МОЙUSER/data/venv/lib/python3.8/site-packages') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings' 
from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application()


через FileZilla удалить из корневой директории все файлы (останется только www/heartem.ru/) и копирую туда все файлы из моего проекта (app, blog_app, static, templates, db.sqlite3, manage.py, passenger_wsgi.py)
открываю свой сайт в браузере!!!
