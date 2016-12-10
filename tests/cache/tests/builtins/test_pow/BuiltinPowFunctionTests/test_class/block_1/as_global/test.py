try:
    print('>>> f = pow')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = pow
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = pow
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = pow
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = pow')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = pow
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
