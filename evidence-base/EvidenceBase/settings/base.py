
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
                  'django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'livereload',
                  'app',
                  'bootstrap3',
                  'accounts',
                  'evidence',
                  'category',
                  'attribute',
                  'board',
                  ]

MIDDLEWARE = [
              'django.middleware.security.SecurityMiddleware',
              'whitenoise.middleware.WhiteNoiseMiddleware',
              'django.contrib.sessions.middleware.SessionMiddleware',
              'django.middleware.common.CommonMiddleware',
              'django.middleware.csrf.CsrfViewMiddleware',
              'django.contrib.auth.middleware.AuthenticationMiddleware',
              'django.contrib.messages.middleware.MessageMiddleware',
              'django.middleware.clickjacking.XFrameOptionsMiddleware',
              ]


ROOT_URLCONF = 'EvidenceBase.urls'

TEMPLATES = [
             {
             'BACKEND': 'django.template.backends.django.DjangoTemplates',
             'DIRS': [TEMPLATE_DIR],
             'APP_DIRS': True,
             'OPTIONS': {
             'context_processors': [
                                    'django.template.context_processors.debug',
                                    'django.template.context_processors.request',
                                    'django.contrib.auth.context_processors.auth',
                                    'django.contrib.messages.context_processors.messages',
                                    ],
             },
             },
             ]

WSGI_APPLICATION = 'EvidenceBase.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
                            {
                            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
                            },
                            {
                            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
                            },
                            {
                            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
                            },
                            {
                            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
                            },
                            ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = (
                    os.path.join(BASE_DIR, "app", "static"),
                    )

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

#THese are Login and Logout page URLs'. They are temporary.
LOGIN_REDIRECT_URL = 'test'
LOGOUT_REDIRECT_URL = 'thanks'

TIME_ZONE = os.getenv("TIME_ZONE")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}
