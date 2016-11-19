try:
    print('>>> f = float')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = float
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = float')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = float
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = float')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = float
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = float')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = float
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
