try:
    print('>>> f = classmethod')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = classmethod
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = classmethod')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = classmethod
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = classmethod')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = classmethod
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = classmethod')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = classmethod
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
