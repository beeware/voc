from .attributes import *
from .klass import Class
from .constants import *
from .fields import Field
from .methods import Method
from .opcodes import *

# Register the MUTF-8 codec
import codecs
from voc.java import mutf_8
codecs.register(mutf_8.search_function)
