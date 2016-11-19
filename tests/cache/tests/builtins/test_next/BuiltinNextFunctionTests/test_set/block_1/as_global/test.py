try:
    print('>>> f = next')
    print('>>> x = set()')
    print('>>> f(x)')
    f = next
    x = set()
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> f = next')
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> f(x)')
    f = next
    x = {1, 2.3456, "another"}
    print(f(x))
except Exception as e:
    print(type(e), ':', e)
print()
