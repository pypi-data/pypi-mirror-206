__version__ = '0.3.1'
__author__ = 'Jonathan Els and Duncan Andrew'

import decimal
import logging

from valr_py.rest_client import *  # noqa
from valr_py.ws_client import *  # noqa

__all__ = (rest_client.__all__, ws_client.__all__)


logging.getLogger(__name__).addHandler(logging.NullHandler())

decimal.getcontext().prec = 8
decimal.DefaultContext.prec = 8
