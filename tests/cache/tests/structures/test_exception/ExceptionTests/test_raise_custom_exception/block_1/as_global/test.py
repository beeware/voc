class MyException(Exception):
    pass

try:
    raise MyException()
except MyException:
    print("Got a custom exception")
print('Done.')
