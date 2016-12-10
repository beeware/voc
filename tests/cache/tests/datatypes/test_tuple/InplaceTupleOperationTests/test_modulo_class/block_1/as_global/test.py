try:
    print('>>> x = (1, 2)')
    print('>>> y = type(1)')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2)
    y = type(1)
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2)')
    print('>>> y = type("a")')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2)
    y = type("a")
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2)')
    print('>>> y = type(object())')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2)
    y = type(object())
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2)')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2)
    y = type("MyClass", (object,), {})
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> y = type(1)')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    y = type(1)
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> y = type("a")')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    y = type("a")
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> y = type(object())')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    y = type(object())
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    y = type("MyClass", (object,), {})
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (3, 1.2, True, )')
    print('>>> y = type(1)')
    print('>>> x %= y')
    print('>>> x')
    x = (3, 1.2, True, )
    y = type(1)
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (3, 1.2, True, )')
    print('>>> y = type("a")')
    print('>>> x %= y')
    print('>>> x')
    x = (3, 1.2, True, )
    y = type("a")
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (3, 1.2, True, )')
    print('>>> y = type(object())')
    print('>>> x %= y')
    print('>>> x')
    x = (3, 1.2, True, )
    y = type(object())
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (3, 1.2, True, )')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x %= y')
    print('>>> x')
    x = (3, 1.2, True, )
    y = type("MyClass", (object,), {})
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2.3456, "another")')
    print('>>> y = type(1)')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2.3456, "another")
    y = type(1)
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2.3456, "another")')
    print('>>> y = type("a")')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2.3456, "another")
    y = type("a")
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2.3456, "another")')
    print('>>> y = type(object())')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2.3456, "another")
    y = type(object())
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = (1, 2.3456, "another")')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x %= y')
    print('>>> x')
    x = (1, 2.3456, "another")
    y = type("MyClass", (object,), {})
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
