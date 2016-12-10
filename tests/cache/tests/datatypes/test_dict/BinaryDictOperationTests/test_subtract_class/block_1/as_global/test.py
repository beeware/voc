try:
    print('>>> x = {}')
    print('>>> y = type(1)')
    print('>>> x - y')
    x = {}
    y = type(1)
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {}')
    print('>>> y = type("a")')
    print('>>> x - y')
    x = {}
    y = type("a")
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {}')
    print('>>> y = type(object())')
    print('>>> x - y')
    x = {}
    y = type(object())
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {}')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x - y')
    x = {}
    y = type("MyClass", (object,), {})
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = type(1)')
    print('>>> x - y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = type(1)
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = type("a")')
    print('>>> x - y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = type("a")
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = type(object())')
    print('>>> x - y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = type(object())
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {"a": 1, "c": 2.3456, "d": "another"}')
    print('>>> y = type("MyClass", (object,), {})')
    print('>>> x - y')
    x = {"a": 1, "c": 2.3456, "d": "another"}
    y = type("MyClass", (object,), {})
    print(x - y)
except Exception as e:
    print(type(e), ':', e)
print()
