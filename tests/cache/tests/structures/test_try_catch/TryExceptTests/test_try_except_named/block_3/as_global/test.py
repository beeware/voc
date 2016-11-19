try:
    obj = int('asdf')
    print('OK')
except NameError as e:
    print("Got a NameError", e)
print('Done.')
