try:
    print('>>> f = round')
    print('>>> x = set()')
    print('>>> f(x)')
    f = round
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = round')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = round
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
