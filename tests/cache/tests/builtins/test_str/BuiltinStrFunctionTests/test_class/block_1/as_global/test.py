try:
    print('>>> f = str')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = str
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = str')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = str
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = str')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = str
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = str')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = str
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
