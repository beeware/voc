try:
    print('>>> f = chr')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = chr
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = chr')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = chr
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = chr')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = chr
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = chr')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = chr
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
