try:
    print('>>> x = slice(0)')
    print('>>> y = NotImplemented')
    print('>>> x **= y')
    print('>>> x')
    x = slice(0)
    y = NotImplemented
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(5)')
    print('>>> y = NotImplemented')
    print('>>> x **= y')
    print('>>> x')
    x = slice(5)
    y = NotImplemented
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7)')
    print('>>> y = NotImplemented')
    print('>>> x **= y')
    print('>>> x')
    x = slice(2, 7)
    y = NotImplemented
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(2, 7, 2)')
    print('>>> y = NotImplemented')
    print('>>> x **= y')
    print('>>> x')
    x = slice(2, 7, 2)
    y = NotImplemented
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -1)')
    print('>>> y = NotImplemented')
    print('>>> x **= y')
    print('>>> x')
    x = slice(7, 2, -1)
    y = NotImplemented
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = slice(7, 2, -2)')
    print('>>> y = NotImplemented')
    print('>>> x **= y')
    print('>>> x')
    x = slice(7, 2, -2)
    y = NotImplemented
    x **= y
    print(x)
except Exception as e:
    print(type(e), ':', e)
print()
