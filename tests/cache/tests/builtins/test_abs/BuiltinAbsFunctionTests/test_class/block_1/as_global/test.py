try:
    print('>>> f = abs')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = abs
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = abs')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = abs
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = abs')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = abs
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = abs')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = abs
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
