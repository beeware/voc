try:
    print('>>> x = bytearray()')
    print('>>> +x')
    x = bytearray()
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray(1)')
    print('>>> +x')
    x = bytearray(1)
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = bytearray([1, 2, 3])')
    print('>>> +x')
    x = bytearray([1, 2, 3])
    print(+x)
except Exception as e:
    print(type(e), ':', e)
print()
