try:
    print('>>> f = isinstance')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = isinstance
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = isinstance')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = isinstance
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = isinstance')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = isinstance
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = isinstance')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = isinstance
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
