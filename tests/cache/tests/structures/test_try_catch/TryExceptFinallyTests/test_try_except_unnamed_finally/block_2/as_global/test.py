try:
    obj.no_such_attribute
    print('OK')
except NameError:
    print("Got an error")
finally:
    print("Do final cleanup")
print('Done.')
