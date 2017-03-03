import codecs

from . import mutf_8
from .attributes import *  # noqa
from .constants import *  # noqa
from .fields import Field  # noqa
from .klass import Class  # noqa
from .methods import Method  # noqa
from .opcodes import *  # noqa

# Register the MUTF-8 codec
codecs.register(mutf_8.search_function)
