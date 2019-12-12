"""
Base settings to build other settings files upon.
"""

import environ
import os
from django.utils.translation import ugettext_lazy as _

env = environ.Env()

ROOT_DIR = (
    environ.Path(__file__) - 3
)  # (smokestack/config/settings/base.py - 3 = smokestack/)
APPS_DIR = ROOT_DIR.path("smokestack")
PROJECT_PATH = env.str('PROJECT_PATH', default=os.path.realpath(APPS_DIR))


# READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
READ_DOT_ENV_FILE = True
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path(".env")))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "UTC"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# TODO: Turn on to do translating sometime?
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = False

# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = (ROOT_DIR.path("locale"),)

LANGUAGES = (
    ('en-us', _('English')),
    ('es-us', _('Spanish')),
)

# Custom stuff
USE_MV = env('USE_MV', default=False)


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {}
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'HOST': env.str('DJANGO_DB_HOST'),
    'NAME': env.str('DJANGO_DB_NAME'),
    'USER': env.str('DJANGO_DB_USER'),
    'PASSWORD': env.str('DJANGO_DB_PASSWORD'),
    'ATOMIC_REQUESTS': True,
}

if USE_MV:
    DATABASES['microvellum'] = {
        'ENGINE': 'sql_server.pyodbc',
        'HOST': '192.168.1.120\\HS_DB',
        'USER': 'mvuser',
        'PASSWORD': 'Microvellum123',
        'NAME': 'MV_Backup',
        # 'PORT': None,
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            # 'driver_supports_utf8': True,
            # 'dsn': 'MVDevelop'
        },
    }
    DATABASE_ROUTERS = ['microvellum.router.MVRouter']


# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    'admin_interface',
    # 'flat_responsive', # only if django version < 2.0
    # 'flat', # only if django version < 1.9
    'colorfield',
    "django.contrib.admin",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    # "allauth.socialaccount",
    "rest_framework",
    'import_export',
    'django_summernote',
]

LOCAL_APPS = [
    "smokestack.users.apps.UsersConfig",
    'smokestack',
    'inventory',
    'tasks'
]

if USE_MV:
    LOCAL_APPS += ['microvellum']

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "smokestack.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# TODO: Enable for more security
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
#     },
#     {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
#     {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
#     {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
# ]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR("staticfiles"))
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR.path("static"))]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR("media"))
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [
            str(APPS_DIR.path("templates")),
            str(APPS_DIR.path("templates/inventory"))],
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "smokestack.utils.context_processors.settings_context",
            ],
        },
    }
]
# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap4"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR.path("fixtures")),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "SAMEORIGIN"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Brad""", "brad@example.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}


# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "username"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "smokestack.users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# SOCIALACCOUNT_ADAPTER = "smokestack.users.adapters.SocialAccountAdapter"


# Your stuff...
# ------------------------------------------------------------------------------

SUMMERNOTE_THEME = 'bs4'
# SUMMERNOTE_CONFIG = {
#     # Using SummernoteWidget - iframe mode, default
#     'iframe': True,

#     # Or, you can set it as False to use SummernoteInplaceWidget by default - no iframe mode
#     # In this case, you have to load Bootstrap/jQuery stuff by manually.
#     # Use this when you're already using Bootstraip/jQuery based themes.
#     # 'iframe': False,

#     # You can put custom Summernote settings
#     'summernote': {
#         # As an example, using Summernote Air-mode
#         'airMode': False,

#         # Change editor size
#         'width': '100%',
#         'height': '480',

#         # Use proper language setting automatically (default)
#         # 'lang': None,

#         # Or, set editor language/locale forcely
#         # 'lang': 'ko-KR',

#         # You can also add custom settings for external plugins
#         # 'print': {
#         #     'stylesheetUrl': '/some_static_folder/printable.css',
#         # },
#         'codemirror': {
#             'mode': 'htmlmixed',
#             'lineNumbers': 'true',
#             # You have to include theme file in 'css' or 'css_for_inplace' before using it.
#             'theme': 'monokai',
#         },
#     },

#     # Need authentication while uploading attachments.
#     # 'attachment_require_authentication': True,

#     # Set `upload_to` function for attachments.
#     # 'attachment_upload_to': my_custom_upload_to_func(),

#     # # Set custom storage class for attachments.
#     # 'attachment_storage_class': 'my.custom.storage.class.name',

#     # # Set custom model for attachments (default: 'django_summernote.Attachment')
#     # 'attachment_model': 'my.custom.attachment.model', # must inherit 'django_summernote.AbstractAttachment'

#     # You can disable attachment feature.
#     'disable_attachment': False,

#     # Set `True` to return attachment paths in absolute URIs.
#     # 'attachment_absolute_uri': False,

#     # test_func in summernote upload view. (Allow upload images only when user passes the test)
#     # https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
#     # ```
#     # def example_test_func(request):
#     #     return request.user.groups.filter(name='group_name').exists()
#     # ```
#     # 'test_func_upload_view': example_test_func,

#     # You can add custom css/js for SummernoteWidget.
#     # 'css': (
#     # ),
#     # 'js': (
#     # ),

#     # You can also add custom css/js for SummernoteInplaceWidget.
#     # !!! Be sure to put {{ form.media }} in template before initiate summernote.
#     # 'css_for_inplace': (
#     # ),
#     # 'js_for_inplace': (
#     # ),

#     # Codemirror as codeview
#     # If any codemirror settings are defined, it will include codemirror files automatically.
#     'css': (
#         '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css',
#     ),

#     # Lazy initialize
#     # If you want to initialize summernote at the bottom of page, set this as True
#     # and call `initSummernote()` on your page.
#     'lazy': True,

#     # To use external plugins,
#     # Include them within `css` and `js`.
#     # 'js': {
#     #     '/some_static_folder/summernote-ext-print.js',
#     #     '//somewhere_in_internet/summernote-plugin-name.js',
#     # },
# }


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
