try:
    print('>>> f = issubclass')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = issubclass
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = issubclass')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = issubclass
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = issubclass')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = issubclass
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = issubclass')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = issubclass
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
