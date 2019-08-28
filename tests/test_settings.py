import os


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    "tests",
]

DATABASES = {
    'default': {
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite'),
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
