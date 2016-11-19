try:
    obj.no_such_attribute
    print('OK')
except AttributeError as e:
    print("Got an AttributeError", e)
except NameError as e:
    print("Got a NameError", e)
print('Done.')
