try:
    print('>>> f = all')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = all
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = all')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = all
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = all')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = all
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = all')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = all
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
