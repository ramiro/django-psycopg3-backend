# A django settings module to run the Django test suite with Postgres

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
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
        "ENGINE": "django.db.backends.postgresql",
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

