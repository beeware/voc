try:
    print('>>> f = frozenset')
    print('>>> x = bytearray()')
    print('>>> f(x)')
    f = frozenset
    x = bytearray()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = frozenset')
    print('>>> x = bytearray(1)')
    print('>>> f(x)')
    f = frozenset
    x = bytearray(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = frozenset')
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> f(x)')
    f = frozenset
    x = bytearray([1, 2, 3])
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
