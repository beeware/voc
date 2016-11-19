try:
    print('>>> x = set()')
    print('>>> ~x')
    x = set()
    print(~x)
except Exception as e:
    print(type(e), ':', e)
print()
##################################################
try:
    print('>>> x = {1, 2.3456, "another"}')
    print('>>> ~x')
    x = {1, 2.3456, "another"}
    print(~x)
except Exception as e:
    print(type(e), ':', e)
print()
