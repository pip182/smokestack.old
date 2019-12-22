from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="pTxpyD7DKjC3MFN9OUZXqHDQB06LfqsrStouS7W9eQgi3SwANeDfE8uhBjkjgMmn",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "192.168.1.201"]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend

EMAIL_HOST = env("DJANGO_EMAIL_HOST", default='smtp.gmail.com')
EMAIL_USE_TLS = env("DJANGO_EMAIL_USE_TLS", default=True)
EMAIL_PORT = env("DJANGO_EMAIL_PORT", default=587)
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER", default='brad.hcf@gmail.com')
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD", default='H0m35te@d12')

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405


if DEBUG:
    if env.bool("DEBUG_TOOLBAR", False):
        # django-debug-toolbars
        # ------------------------------------------------------------------------------
        # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
        INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
        # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
        MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
        # https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
        DEBUG_TOOLBAR_CONFIG = {
            "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
            "SHOW_TEMPLATE_CONTEXT": True,
        }
        # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
        INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]


# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405

# Your stuff...
# ------------------------------------------------------------------------------
