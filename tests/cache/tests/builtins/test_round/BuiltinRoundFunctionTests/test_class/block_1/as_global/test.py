try:
    print('>>> f = round')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = round
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = round')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = round
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = round')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = round
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = round')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = round
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
