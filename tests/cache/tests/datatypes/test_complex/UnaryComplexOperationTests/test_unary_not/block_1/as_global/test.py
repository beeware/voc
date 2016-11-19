try:
    print('>>> x = 1j')
    print('>>> not x')
    x = 1j
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 3.14159265j')
    print('>>> not x')
    x = 3.14159265j
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 1+2j')
    print('>>> not x')
    x = 1+2j
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 3-4j')
    print('>>> not x')
    x = 3-4j
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = -5j')
    print('>>> not x')
    x = -5j
    print(not x)
except Exception as e:
    print(type(e), ':', e)
print()
