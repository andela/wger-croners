import dj_database_url
import settings_global
import settings


DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']