try:
    obj = 3
    print('OK')
except NameError:
    print("Got a NameError")
except AttributeError as e:
    print("Got an AttributeError", e)
else:
    print("Do else handling")
print('Done.')
