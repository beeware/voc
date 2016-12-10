try:
    print('>>> f = set')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = set
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = set')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = set
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = set')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = set
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = set')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = set
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
