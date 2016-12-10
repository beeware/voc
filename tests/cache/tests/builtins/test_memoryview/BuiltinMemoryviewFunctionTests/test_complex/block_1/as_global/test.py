try:
    print('>>> f = memoryview')
    print('>>> x = 1j')
    print('>>> f(x)')
    f = memoryview
    x = 1j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = 3.14159265j')
    print('>>> f(x)')
    f = memoryview
    x = 3.14159265j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = 1+2j')
    print('>>> f(x)')
    f = memoryview
    x = 1+2j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = 3-4j')
    print('>>> f(x)')
    f = memoryview
    x = 3-4j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = memoryview')
    print('>>> x = -5j')
    print('>>> f(x)')
    f = memoryview
    x = -5j
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
