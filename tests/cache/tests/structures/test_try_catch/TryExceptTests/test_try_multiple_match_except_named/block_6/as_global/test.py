try:
    obj = int('asdf')
    print('OK')
except (NameError, TypeError) as e:
    print("Got a NameError or TypeError", e)
except AttributeError as e:
    print("Got an AttributeError", e)
print('Done.')
