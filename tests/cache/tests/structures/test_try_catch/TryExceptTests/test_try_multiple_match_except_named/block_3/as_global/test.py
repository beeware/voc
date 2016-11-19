try:
    obj.no_such_attribute
    print('OK')
except (TypeError, NameError) as e:
    print("Got a TypeError or NameError", e)
except AttributeError as e:
    print("Got an AttributeError", e)
print('Done.')
