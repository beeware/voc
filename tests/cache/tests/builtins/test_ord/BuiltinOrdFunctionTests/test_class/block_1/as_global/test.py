try:
    print('>>> f = ord')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = ord
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ord')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = ord
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ord')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = ord
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = ord')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = ord
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
