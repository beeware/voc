try:
    obj = int('asdf')
    print('OK')
except NameError:
    print("Got an error")
else:
    print("Do else handling")
print('Done.')
