try:
    print('>>> x = set()')
    print('>>> y = NotImplemented')
    print('>>> x <= y')
    x = set()
    y = NotImplemented
    print(x <= y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> y = NotImplemented')
    print('>>> x <= y')
    x = {1, 2.3456, "another"}
    y = NotImplemented
    print(x <= y)
except Exception as e:
    print(type(e), ':', e)
print()
