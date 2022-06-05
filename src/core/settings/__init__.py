from .base import *

DEBUG = int(os.environ.get("DEBUG", default="1"))

if DEBUG:
    from .dev import *
else:
    from .prod import *
