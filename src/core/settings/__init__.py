from .base import *

DEBUG = int(os.environ.get("DEBUG"))

if DEBUG:
    from .dev import *
else:
    from .prod import *
