import codecs

from . import mutf_8
from .attributes import *
from .constants import *
from .fields import Field
from .klass import Class
from .methods import Method
from .opcodes import *

# Register the MUTF-8 codec
codecs.register(mutf_8.search_function)
