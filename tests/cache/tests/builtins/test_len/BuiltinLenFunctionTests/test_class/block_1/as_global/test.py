try:
    print('>>> f = len')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = len
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = len
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = len
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = len')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = len
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
