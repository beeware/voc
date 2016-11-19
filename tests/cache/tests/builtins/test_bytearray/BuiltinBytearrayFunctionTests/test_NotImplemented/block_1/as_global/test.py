try:
    print('>>> f = bytearray')
    print('>>> x = NotImplemented')
    print('>>> f(x)')
    f = bytearray
    x = NotImplemented
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
