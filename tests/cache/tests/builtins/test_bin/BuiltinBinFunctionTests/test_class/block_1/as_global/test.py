try:
    print('>>> f = bin')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = bin
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bin')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = bin
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bin')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = bin
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bin')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = bin
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
