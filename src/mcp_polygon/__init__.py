# from .routes.alt import *
# from .routes.benzinga import *
from .routes.crypto import *
from .routes.forex import *
# from .routes.futures import *
from .routes.meta import *
from .routes.options import *
from .routes.stocks import *

from .server import run

__all__ = [
    "run",
]