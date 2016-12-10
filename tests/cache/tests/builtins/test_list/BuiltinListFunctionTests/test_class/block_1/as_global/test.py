try:
    print('>>> f = list')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = list
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = list')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = list
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = list')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = list
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = list')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = list
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
