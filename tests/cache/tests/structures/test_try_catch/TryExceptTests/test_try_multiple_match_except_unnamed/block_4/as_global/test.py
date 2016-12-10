try:
    obj.no_such_attribute
    print('OK')
except AttributeError:
    print("Got an AttributeError")
except (NameError, TypeError):
    print("Got a NameError or TypeError")
print('Done.')
