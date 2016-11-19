try:
    print('>>> f = min')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = min
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = min')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = min
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = min')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = min
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = min')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = min
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
