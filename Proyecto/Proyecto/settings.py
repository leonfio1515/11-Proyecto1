from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p#wyp2+j8s5t$_30)-t8tvx%eq852na1$(yy)%cxrf#jz*$b14'

# SECURITY WARNING: don't run with debug turned on in production!



# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'rangefilter',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'colorfield',

    'CajasApp',
    'FuncionariosApp',
    'FormulariosApp',
    'AdministracionApp',
    'AdmCajasApp',
    'AdmConveniosApp',
    'User',
    'Login',

    'import_export',
]

X_FRAME_OPTIONS = "SAMEORIGIN"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'crum.CurrentRequestUserMiddleware',

]

ROOT_URLCONF = 'Proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [

            BASE_DIR / 'AdmCajasApp/templates/List',

            BASE_DIR / 'AdministracionApp/templates/Form',
            BASE_DIR / 'AdministracionApp/templates/List',
            BASE_DIR / 'AdministracionApp/templates/Update',

            BASE_DIR / 'CajasApp/templates/List',
            BASE_DIR / 'CajasApp/templates/Detail',

            BASE_DIR / 'FormulariosApp/templates/Form',
            BASE_DIR / 'FormulariosApp/templates/List',
            BASE_DIR / 'FormulariosApp/templates/Update',
            BASE_DIR / 'FormulariosApp/templates/Detail',

            BASE_DIR / 'Login/templates',

            BASE_DIR / 'templates/Inicio',
            BASE_DIR / 'templates/Institucional',

            BASE_DIR/ 'Proyecto/templates/login',

        ],
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

WSGI_APPLICATION = 'Proyecto.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-la'

TIME_ZONE = 'America/Montevideo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/




STATIC_URL = 'static/'
MEDIA_URL = 'media/'



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')


STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '../../login/login'
LOGIN_REDIRECT_URL='inicio'

DATA_UPLOAD_MAX_MEMORY_SIZE = 1000000000
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

AUTH_USER_MODEL = 'User.Usuario'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#Ejecutar python manage.py collectstatic --noinput
#Debe crear carpeta static_root



DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# db_from_env = dj_database_url.config(conn_max_age=500)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'project',
#         'USER': 'postgres',
#         'PASSWORD': '210703920014Leo',
#         'HOST': '127.0.0.1',
#         'PORT': 5432,

#     }
# }


