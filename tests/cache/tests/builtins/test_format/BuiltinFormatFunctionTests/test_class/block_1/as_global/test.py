try:
    print('>>> f = format')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = format
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = format')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = format
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = format')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = format
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = format')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = format
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
