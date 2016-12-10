try:
    print('>>> f = slice')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = slice
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = slice')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = slice
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = slice')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = slice
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = slice')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = slice
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
