try:
    print('>>> f = __import__')
    print('>>> x = set()')
    print('>>> f(x)')
    f = __import__
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = __import__')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = __import__
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
