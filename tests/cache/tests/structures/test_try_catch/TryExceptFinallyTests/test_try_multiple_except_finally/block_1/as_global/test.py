try:
    obj = 3
    print('OK')
except NameError:
    print("Got a NameError")
except AttributeError as e:
    print("Got an AttributeError", e)
finally:
    print("Do final cleanup")
print('Done.')
