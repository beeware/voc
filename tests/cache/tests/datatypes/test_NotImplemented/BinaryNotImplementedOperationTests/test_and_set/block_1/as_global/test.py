try:
    print('>>> x = NotImplemented')
    print('>>> y = set()')
    print('>>> x & y')
    x = NotImplemented
    y = set()
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = NotImplemented')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x & y')
    x = NotImplemented
    y = {1, 2.3456, "another"}
    print(x & y)
except Exception as e:
    print(type(e), ':', e)
print()
