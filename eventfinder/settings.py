import os
import dj_database_url

# Replace the existing DATABASES configuration with:
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Add this line to the MIDDLEWARE list, after SecurityMiddleware:
'whitenoise.middleware.WhiteNoiseMiddleware',

# Update ALLOWED_HOSTS
ALLOWED_HOSTS = ['yourdomain.onrender.com', 'localhost', '127.0.0.1']

# Set DEBUG based on environment variable
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Update STATIC_ROOT and add STATICFILES_STORAGE
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
