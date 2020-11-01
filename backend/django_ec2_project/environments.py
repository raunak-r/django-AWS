import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEV = {
    'STATIC_ROOT': os.path.join(BASE_DIR, 'staticfiles'),
    'STATIC_URL': '/static/',
    'DOMAIN': os.environ.get('domain', '127.0.0.1'),
    'DEBUG': os.environ.get('debug', True),
    'ALLOWED_HOSTS': ['localhost', '127.0.0.1', '*', os.environ.get('allowed_hosts')],
    'DATABASES': {
    	'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': os.environ.get('db_name', os.path.join(BASE_DIR, 'db.sqlite3')),
    	}
    },
}

CURR_ENV = DEV