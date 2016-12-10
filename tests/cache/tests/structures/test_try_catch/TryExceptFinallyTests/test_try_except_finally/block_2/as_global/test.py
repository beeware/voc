try:
    obj.no_such_attribute
    print('OK')
except:
    print("Got an error")
finally:
    print("Do final cleanup")
print('Done.')
