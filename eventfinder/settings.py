import os
import dj_database_url

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Middleware configuration
MIDDLEWARE = [
    # ... other middleware ...
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line after SecurityMiddleware
    # ... rest of your middleware ...
]

# Update ALLOWED_HOSTS
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Set DEBUG based on environment variable
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Static files configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Make sure you have these settings for handling static files
STATIC_URL = '/static/'

# If you're using django-environ, make sure to load the .env file
# import environ
# env = environ.Env()
# environ.Env.read_env()

# Secret key configuration
SECRET_KEY = os.environ.get('SECRET_KEY')

# Email configuration
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# OpenCage API configuration
OPENCAGE_API_KEY = os.environ.get('OPENCAGE_API_KEY')

# ... rest of your settings ...
