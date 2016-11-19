try:
    print('>>> f = memoryview')
    print('>>> x = type(1)')
    print('>>> f(x)')
    f = memoryview
    x = type(1)
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = type("a")')
    print('>>> f(x)')
    f = memoryview
    x = type("a")
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = type(object())')
    print('>>> f(x)')
    f = memoryview
    x = type(object())
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = type("MyClass", (object,), {})')
    print('>>> f(x)')
    f = memoryview
    x = type("MyClass", (object,), {})
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
