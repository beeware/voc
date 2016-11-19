try:
    print('>>> x = set()')
    print('>>> not x')
    x = set()
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> not x')
    x = {1, 2.3456, "another"}
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
