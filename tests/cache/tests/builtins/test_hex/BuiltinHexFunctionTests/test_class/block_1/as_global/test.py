try:
    print('>>> f = hex')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = hex
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hex')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = hex
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hex')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = hex
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = hex')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = hex
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
