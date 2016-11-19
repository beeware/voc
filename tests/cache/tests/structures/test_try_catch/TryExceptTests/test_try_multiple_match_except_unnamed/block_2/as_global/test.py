try:
    obj.no_such_attribute
    print('OK')
except (NameError, TypeError):
    print("Got a NameError or TypeError")
except AttributeError:
    print("Got an AttributeError")
print('Done.')
