try:
    print('>>> x = {}')
    print('>>> y = b""')
    print('>>> x **= y')
    print('>>> x')
    x = {}
    y = b""
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {}')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x **= y')
    print('>>> x')
    x = {}
    y = b"This is another string of bytes"
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = b""')
    print('>>> x **= y')
    print('>>> x')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = b""
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = b"This is another string of bytes"')
    print('>>> x **= y')
    print('>>> x')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = b"This is another string of bytes"
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
