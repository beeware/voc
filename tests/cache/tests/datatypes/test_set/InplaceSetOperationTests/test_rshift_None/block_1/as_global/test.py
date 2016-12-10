try:
    print('>>> x = set()')
    print('>>> y = None')
    print('>>> x >>= y')
    print('>>> x')
    x = set()
    y = None
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = None')
    print('>>> x >>= y')
    print('>>> x')
    x = {1, 2.3456, "another"}
    y = None
    x >>= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
