try:
    print('>>> f = bool')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = bool
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bool')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = bool
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bool')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = bool
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = bool')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = bool
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
