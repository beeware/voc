from example import *

try:
    raise MyException("This is the exception")
except MyException:
    print("Got a custom exception")
print('Done.')
