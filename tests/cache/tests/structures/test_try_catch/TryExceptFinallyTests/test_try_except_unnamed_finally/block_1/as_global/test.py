try:
    obj = 3
    print('OK')
except NameError:
    print("Got an error")
finally:
    print("Do final cleanup")
print('Done.')
