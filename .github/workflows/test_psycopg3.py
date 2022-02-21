# A django settings module to run the Django test suite using Psycopg 3.

DATABASES = {
    "default": {
        "ENGINE": "django_psycopg3",
        "HOST": "localhost",
        # "NAME": "django",
        # "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "TEST": {
            "NAME": "test_django",
        },
    },
    "other": {
        "ENGINE": "django_psycopg3",
        "HOST": "localhost",
        # "NAME": "django2",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "TEST": {
            "NAME": "test_other",
        },
    },
}

INSTALLED_APPS = [
    "django.contrib.postgres"
]

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

USE_TZ = False
