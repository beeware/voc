try:
    print('>>> f = help')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = help
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = help')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = help
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = help')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = help
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = help')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = help
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
