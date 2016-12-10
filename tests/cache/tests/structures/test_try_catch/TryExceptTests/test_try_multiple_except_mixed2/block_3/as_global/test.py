try:
    obj = int('asdf')
    print('OK')
except NameError as e:
    print("Got a NameError", e)
except AttributeError:
    print("Got an AttributeError")
print('Done.')
