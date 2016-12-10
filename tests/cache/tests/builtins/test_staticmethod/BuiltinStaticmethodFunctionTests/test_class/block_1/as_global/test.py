try:
    print('>>> f = staticmethod')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = staticmethod
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = staticmethod')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = staticmethod
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = staticmethod')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = staticmethod
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = staticmethod')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = staticmethod
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
