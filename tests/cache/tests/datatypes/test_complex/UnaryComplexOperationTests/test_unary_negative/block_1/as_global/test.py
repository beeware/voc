try:
    print('>>> x = 1j')
    print('>>> -x')
    x = 1j
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 3.14159265j')
    print('>>> -x')
    x = 3.14159265j
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 1+2j')
    print('>>> -x')
    x = 1+2j
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = 3-4j')
    print('>>> -x')
    x = 3-4j
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = -5j')
    print('>>> -x')
    x = -5j
    print(-x)
except Exception as e:
    print(type(e), ':', e)
print()
