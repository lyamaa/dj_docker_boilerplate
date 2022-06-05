import os

import dj_database_url

from .base import *


DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASES["default"] = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=500, ssl_require=True
)

STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
