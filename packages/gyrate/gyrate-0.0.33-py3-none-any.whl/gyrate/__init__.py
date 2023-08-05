# -*- coding: utf-8 -*-

import logging

from .gyrate import Spinner
from gyrate._constants import search_for
from .notebook import Notebook

search_for()

logging.getLogger(__name__).addHandler(logging.NullHandler())
