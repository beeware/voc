try:
    obj.no_such_attribute
    print('OK')
except:
    print("Got an error")
else:
    print("Do else handling")
print('Done.')
