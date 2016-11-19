try:
    print('>>> x = True')
    print('>>> y = type(1)')
    print('>>> x ^ y')
    x = True
    y = type(1)
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = type("a")')
    print('>>> x ^ y')
    x = True
    y = type("a")
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = type(object())')
    print('>>> x ^ y')
    x = True
    y = type(object())
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = True')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x ^ y')
    x = True
    y = type("MyClass", (object,), {})
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = type(1)')
    print('>>> x ^ y')
    x = False
    y = type(1)
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = type("a")')
    print('>>> x ^ y')
    x = False
    y = type("a")
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = type(object())')
    print('>>> x ^ y')
    x = False
    y = type(object())
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = False')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x ^ y')
    x = False
    y = type("MyClass", (object,), {})
    print(x ^ y)
except Exception as e:
    print(type(e), ':', e)
print()
