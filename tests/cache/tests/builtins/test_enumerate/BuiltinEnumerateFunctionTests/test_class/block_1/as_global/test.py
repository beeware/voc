try:
    print('>>> f = enumerate')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = enumerate
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = enumerate
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = enumerate
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = enumerate
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
