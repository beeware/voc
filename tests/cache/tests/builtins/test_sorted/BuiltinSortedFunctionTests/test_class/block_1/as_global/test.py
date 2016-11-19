try:
    print('>>> f = sorted')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = sorted
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sorted')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = sorted
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sorted')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = sorted
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = sorted')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = sorted
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
