#Development setup instructions

install django:
```python -m pip install django```

install django REST framework:
```python -m pip install djangorestframework```

check install and version:
```django-admin --version```

Start a django project:
```django-admin startproject budget_buddy```

install MySQL-python, which is a database connector for Python:
```python -m pip install MySQL-python  xxxx```

do
```python -m pip install mysqlclient-1.3.9-cp36-cp36m-win_amd64.whl```


in settings.py 
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'budget_buddy',
	'rest_framework',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'budbud_db',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
```
Create your new app:
```$ python manage.py startapp budget_buddy```


```python manage.py migrate```


```python manage.py runserver```

