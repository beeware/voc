try:
    print('>>> f = enumerate')
    print('>>> x = set()')
    print('>>> f(x)')
    f = enumerate
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = enumerate')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = enumerate
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
