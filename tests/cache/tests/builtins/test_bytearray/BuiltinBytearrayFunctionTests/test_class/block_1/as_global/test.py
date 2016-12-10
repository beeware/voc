try:
    print('>>> f = bytearray')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = bytearray
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytearray')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = bytearray
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytearray')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = bytearray
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bytearray')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = bytearray
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
