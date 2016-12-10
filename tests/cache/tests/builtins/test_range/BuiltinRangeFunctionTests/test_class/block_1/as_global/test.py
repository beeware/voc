try:
    print('>>> f = range')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = range
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = range')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = range
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = range')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = range
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = range')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = range
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
