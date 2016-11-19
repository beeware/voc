try:
    print('>>> f = bytearray')
    print('>>> x = None')
    print('>>> f(x)')
    f = bytearray
    x = None
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
