"""
Django settings for {{ project_name }} project in production mode

This fill will be automatically used when using a dedicated application server.
See `base.py` for basic settings.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""


from .base import *


DEBUG = False

# Remember to set SECRET_KEY in local.py

# remember to set this to your expected hostnames
ALLOWED_HOSTS = []


# file and console logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "main": {
            "format": "{asctime}:{levelname}:{name}: {message} ({filename}:{lineno})",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "main",
        },
        "file": {
            "level": "WARNING",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "YOUR-LOGFILE-PATH-HERE.log",
            "maxBytes": 1024 * 1024 * 10,
            "backupCount": 10,
            "formatter": "main",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["console", "file"],
            "level": "ERROR",
            "propagate": False,
        },
        "": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
    },
}
