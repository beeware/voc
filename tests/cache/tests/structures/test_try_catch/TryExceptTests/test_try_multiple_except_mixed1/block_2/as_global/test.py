try:
    obj.no_such_attribute
    print('OK')
except NameError:
    print("Got a NameError")
except AttributeError as e:
    print("Got an AttributeError", e)
print('Done.')
