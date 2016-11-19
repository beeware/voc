try:
    print('>>> f = tuple')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = tuple
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = tuple')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = tuple
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = tuple')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = tuple
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = tuple')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = tuple
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
