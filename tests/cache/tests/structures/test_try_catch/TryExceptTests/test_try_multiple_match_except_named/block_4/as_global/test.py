try:
    obj.no_such_attribute
    print('OK')
except AttributeError as e:
    print("Got an AttributeError", e)
except (NameError, TypeError) as e:
    print("Got a NameError or TypeError", e)
print('Done.')
