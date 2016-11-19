try:
    print('>>> f = eval')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = eval
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = eval')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = eval
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = eval')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = eval
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = eval')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = eval
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
