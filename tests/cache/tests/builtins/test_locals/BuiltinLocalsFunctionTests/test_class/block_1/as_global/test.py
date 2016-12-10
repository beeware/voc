try:
    print('>>> f = locals')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = locals
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = locals
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = locals
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = locals')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = locals
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
