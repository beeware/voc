try:
    print('>>> f = bytearray')
    print('>>> x = set()')
    print('>>> f(x)')
    f = bytearray
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytearray')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = bytearray
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
