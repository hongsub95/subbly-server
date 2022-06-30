from .common import *

DEBUG = False

ALLOWED_HOSTS = [
<<<<<<< HEAD
    "54.180.94.49",
    "127.0.0.1"
] 
=======
    "54.180.94.49"
]
>>>>>>> fefd20cd0a6f195f673b0bed9376fbaf80db2eaf

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "users.apps.UsersConfig",
    "core.apps.CoreConfig",
    "clothes.apps.ClothesConfig",
    "markets.apps.MarketsConfig",
    "options.apps.OptionsConfig",
    "lists.apps.ListsConfig",
]

THIRD_APPS = [
    "bootstrap5",
    "rest_framework",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_APPS
