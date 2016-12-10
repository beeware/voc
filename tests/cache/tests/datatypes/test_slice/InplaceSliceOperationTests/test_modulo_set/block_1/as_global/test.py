try:
    print('>>> x = slice(0)')
    print('>>> y = set()')
    print('>>> x %= y')
    print('>>> x')
    x = slice(0)
    y = set()
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(0)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x %= y')
    print('>>> x')
    x = slice(0)
    y = {1, 2.3456, "another"}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(5)')
    print('>>> y = set()')
    print('>>> x %= y')
    print('>>> x')
    x = slice(5)
    y = set()
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(5)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x %= y')
    print('>>> x')
    x = slice(5)
    y = {1, 2.3456, "another"}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7)')
    print('>>> y = set()')
    print('>>> x %= y')
    print('>>> x')
    x = slice(2, 7)
    y = set()
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x %= y')
    print('>>> x')
    x = slice(2, 7)
    y = {1, 2.3456, "another"}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7, 2)')
    print('>>> y = set()')
    print('>>> x %= y')
    print('>>> x')
    x = slice(2, 7, 2)
    y = set()
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7, 2)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x %= y')
    print('>>> x')
    x = slice(2, 7, 2)
    y = {1, 2.3456, "another"}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -1)')
    print('>>> y = set()')
    print('>>> x %= y')
    print('>>> x')
    x = slice(7, 2, -1)
    y = set()
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -1)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x %= y')
    print('>>> x')
    x = slice(7, 2, -1)
    y = {1, 2.3456, "another"}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -2)')
    print('>>> y = set()')
    print('>>> x %= y')
    print('>>> x')
    x = slice(7, 2, -2)
    y = set()
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -2)')
    print('>>> y = {1, 2.3456, "another"}')
    print('>>> x %= y')
    print('>>> x')
    x = slice(7, 2, -2)
    y = {1, 2.3456, "another"}
    x %= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
