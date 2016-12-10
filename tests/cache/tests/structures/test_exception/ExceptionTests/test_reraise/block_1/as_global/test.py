try:
    raise KeyError("This is the name")
    print("No error")
except KeyError:
    print("Got error")
    raise
print('Done.')
